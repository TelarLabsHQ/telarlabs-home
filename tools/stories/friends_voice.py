"""Narration for 'Friends Around the World' with correct names and greetings.
Words in IPA are spliced into the phonemes, so the voice never spells them out like acronyms."""
import re, subprocess, soundfile as sf
from kokoro_onnx import Kokoro
K = Kokoro('/tmp/kok/kokoro-v1.0.onnx', '/tmp/kok/voices-v1.0.bin')
OUT = '/home/claude/telarlabs-home/public/stories-demo/assets/voice/friends/'
IPA = {   # word as written -> how it should sound
 'Amara': 'ɐmˈɑːɹə', 'Paolo': 'pˈaʊloʊ', 'Zofia': 'zˈoʊfiːjɑː', 'Ayaan': 'ɑːjˈɑːɑːn', 'Lena': 'lˈeɪnə',
 'Kumusta': 'kuːmˈuːstɑː', 'lola': 'lˈɔːlɑː', 'pancit': 'pɑːnsˈɪt', 'Cześć': 'tʃˈɛʃtʃ', 'pierogi': 'pɪɹˈoʊɡi',
 'Assalam-o-alaikum': 'ɑːsɑːlˈɑːm mɑːlˈeɪkɔm', 'Hallo': 'hɑːlˈuː', 'Bawo ni': 'bˈɔː nɪ', 'jollof': 'dʒˈɑːləf',
 'Yoruba': 'jˈɔːɹʊbə', 'Urdu': 'ˈʊɹduː', 'samosas': 'səmˈoʊsəz', 'Ms.': 'mˈɪz',
}
SCENES = [
 'Friends Around the World',
 "It was Amara's first day at a new school. Her family had just moved from Nigeria, and she didn't know anyone yet.",
 '"Class, this is Amara," said Ms. Rose. "Tomorrow is Share Your Home Day. Bring something special from your family\'s country!"',
 'The next day, Paolo went first. "Kumusta! That\'s hello in Filipino. My lola makes pancit, long noodles for a long and happy life!"',
 'Zofia waved. "Cześć! That\'s hi in Polish. These are pierogi, little dumplings my grandma fills with potato and cheese."',
 'Ayaan smiled. "Assalam-o-alaikum! That means peace be with you, in Urdu. In Pakistan, we share samosas with friends."',
 'Lena held up a big pretzel. "Hallo! That\'s hello in German. In Germany, we love soft pretzels for a snack."',
 'Then it was Amara\'s turn. Her voice was small. "Bawo ni! That\'s hello in Yoruba, one of the languages of Nigeria. This is jollof rice. My mom makes it for every celebration."',
 'Everyone wanted to try it! "This is delicious!" said Paolo. At lunch, they shared all the food, and Amara laughed for the first time all week.',
 'We come from different places, but a smile means hello everywhere. And that is how Amara found friends from around the world.',
]
PAT = re.compile(r"((?:" + '|'.join(sorted(map(re.escape, IPA), key=len, reverse=True)) + r")(?:'s)?)(?=\W|$)")
def phonemes(text):
    text = re.sub('["“”]', '', text)
    out = []
    for i, part in enumerate(PAT.split(text)):
        if not part: continue
        if i % 2: out.append(IPA[part[:-2]] + 'z' if part.endswith("'s") else IPA[part])   # Amara's
        elif part.strip(): out.append(K.tokenizer.phonemize(part, 'en-us').strip())
    s = ' '.join(out)
    return re.sub(r' +([,.!?;:])', r'\1', s)
if __name__ == '__main__':
    for i, t in enumerate(SCENES, 1):
        ph = phonemes(t); print(i, ph)
        a, sr = K.create(ph, voice='af_heart', speed=0.95, lang='en-us', is_phonemes=True)
        sf.write('/tmp/v.wav', a, sr)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', '/tmp/v.wav', '-ac', '1', '-c:a', 'aac', '-b:a', '64k', f'{OUT}s{i}.m4a'], check=True)
        print(' ', round(len(a) / sr, 1), 's', flush=True)
