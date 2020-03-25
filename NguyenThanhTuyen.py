# Nguyễn Thanh Tuyên - 16022145
# Nộp bài thu âm cơ bản

import sounddevice
from scipy.io.wavfile import write

fs = 44100
second = 15
print ("recoding....")
myrecording = sounddevice.rec(int(second * fs), samplerate = fs, channels =2)
sounddevice.wait()
write('output.wav',fs,myrecording)