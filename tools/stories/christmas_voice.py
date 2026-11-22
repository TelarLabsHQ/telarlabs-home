"""Re-voice 'The Christmas Gift' scenes that say "Mr. Ben": Mr. is spliced in as phonemes so there is no pause after it."""
import re, subprocess, soundfile as sf
from kokoro_onnx import Kokoro
K = Kokoro('/tmp/kok/kokoro-v1.0.onnx', '/tmp/kok/voices-v1.0.bin')
OUT = '/home/claude/telarlabs-home/public/stories-demo/assets/voice/christmas-gift/'
SCENES = {
 4: 'On the way home, Lily saw Mr. Ben, her old neighbor. He was sitting by his window, all alone, just like every night.',
 5: '"Mom, why is Mr. Ben always alone?" Lily asked. "His family lives far away," said Mom. "Christmas can feel lonely for him."',
 6: 'Lily looked at her coin jar. She thought about the snow globe. Then she thought about Mr. Ben. And she had an idea.',
 8: 'On Christmas Eve, Lily knocked on Mr. Ben\'s door. The card said: "Merry Christmas, Mr. Ben! You are not alone."',
 9: 'Mr. Ben smiled the biggest smile. "This is the best gift I\'ve had in years," he said. Together, they sang Christmas songs.',
}
def phonemes(text):
    text = re.sub('["“”]', '', text).replace('Mr. Ben', 'Mister Ben')
    s = K.tokenizer.phonemize(text, 'en-us').strip()
    return s
if __name__ == '__main__':
    import sys
    for i, t in SCENES.items():
        ph = phonemes(t); print(i, ph)
        a, sr = K.create(ph, voice='af_heart', speed=0.95, lang='en-us', is_phonemes=True)
        sf.write(f'/tmp/cg{i}.wav', a, sr)
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'/tmp/cg{i}.wav','-ac','1','-c:a','aac','-b:a','64k',f'{OUT}s{i}.m4a'], check=True)
        print(' ', round(len(a)/sr,1), 's', flush=True)
