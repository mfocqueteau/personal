""" module_doctsring """
import soundfile as sf
import simpleaudio as sa
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft

data, samplerate = sf.read('rBRuG4GMZ98.flac')
print(f'{len(data) / samplerate = }')
print(f'{data.shape = }')

length = len(data[0])
start, end = length // 3, length * 2 // 3

trans = fft(data[0])
plt.subplot(211)
plt.plot(data)
plt.subplot(212)
plt.plot(np.real(trans))
plt.show()
