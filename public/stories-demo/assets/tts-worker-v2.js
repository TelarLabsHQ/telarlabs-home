// Runs the Kokoro AI voice in the background so the editor never freezes.
let tts=null, loading=null;
const OWN='https://media.telarlabs.net/stories/', OWN_MODEL='kokoro-82m-v1.0';
function useHF(){ const E=globalThis.__tfenv; if(E){E.remoteHost='https://huggingface.co/'; E.remotePathTemplate='{model}/resolve/{revision}/';} globalThis.KOKORO_VOICES=''; }
async function load(){
  if(tts) return tts;
  if(!loading) loading=(async()=>{
    const mod=await import('./kokoro.web.js?r2');
    mod.env.wasmPaths=new URL('./ort-v2/',import.meta.url).href;
    const files={};
    const opts={dtype:'q8',device:'wasm',
      progress_callback:p=>{ if(p.status==='progress'){ files[p.file]=[p.loaded||0,p.total||0];
        let l=0,t=0; for(const k in files){l+=files[k][0];t+=files[k][1];}
        postMessage({type:'progress',pct:t?Math.round(l/t*100):null,mb:Math.round(l/1048576)}); } }};
    const E=globalThis.__tfenv; if(E) E.allowLocalModels=false;
    // The voice model is stored on our own media server (Cloudflare R2); Hugging Face is the backup.
    try{
      if(!E) throw new Error('no env');
      E.remoteHost=OWN; E.remotePathTemplate='{model}/'; globalThis.KOKORO_VOICES=OWN+OWN_MODEL+'/voices/';
      tts=await mod.KokoroTTS.from_pretrained(OWN_MODEL,opts);
    }catch(err){
      console.warn('voice model: using backup host',err);
      useHF(); for(const k in files) delete files[k];
      tts=await mod.KokoroTTS.from_pretrained('onnx-community/Kokoro-82M-v1.0-ONNX',opts);
    }
    postMessage({type:'ready'});
    return tts;
  })().catch(e=>{loading=null;throw e;});
  return loading;
}
postMessage({type:'alive'});
onmessage=async e=>{
  const {id,text,voice,speed}=e.data;
  try{
    const m=await load();
    let out;
    try{ out=await m.generate(text,{voice,speed}); }
    catch(err){ if(!globalThis.KOKORO_VOICES) throw err; useHF(); out=await m.generate(text,{voice,speed}); }  // voice file: backup host
    const audio=out.audio;
    postMessage({type:'done',id,audio,sr:out.sampling_rate||24000},[audio.buffer]);
  }catch(err){ postMessage({type:'error',id,msg:String(err&&err.message||err)}); }
};
