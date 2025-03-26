from orpheus_cpp import OrpheusCpp
from scipy.io.wavfile import write


orpheus = OrpheusCpp()

text = "zac: I really hope the project deadline doesn't get moved up again."

sample_rate, samples = orpheus.tts(text)
write("output.wav", sample_rate, samples.squeeze())
