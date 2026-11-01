// Runs the Kokoro AI voice in the background so the editor never freezes.
let tts=null, loading=null;
async function load(){
  if(tts) return tts;
  if(!loading) loading=(async()=>{
    const mod=await import('./kokoro.web.js');
    mod.env.wasmPaths=new URL('./ort-v2/',import.meta.url).href;
    const files={};
    tts=await mod.KokoroTTS.from_pretrained('onnx-community/Kokoro-82M-v1.0-ONNX',{dtype:'q8',device:'wasm',
      progress_callback:p=>{ if(p.status==='progress'){ files[p.file]=[p.loaded||0,p.total||0];
        let l=0,t=0; for(const k in files){l+=files[k][0];t+=files[k][1];}
        postMessage({type:'progress',pct:t?Math.round(l/t*100):null,mb:Math.round(l/1048576)}); } }});
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
    const out=await m.generate(text,{voice,speed});
    const audio=out.audio;
    postMessage({type:'done',id,audio,sr:out.sampling_rate||24000},[audio.buffer]);
  }catch(err){ postMessage({type:'error',id,msg:String(err&&err.message||err)}); }
};
