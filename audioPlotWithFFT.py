import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
try:
    audio = pyaudio.PyAudio()
except OSError as e:
    print(f"Error initializing PyAudio: {e}")
    exit(1)
try:
    stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
except OSError as e:
    print(f"Error opening audio stream: {e}")
    exit(1)
    
#matplot properties
fig, ax = plt.subplots()
x = np.linspace(0, RATE // 2,CHUNK // 2)
line, =ax.plot(x, np.random.rand(CHUNK // 2))
ax.set_ylim(0,1000)
ax.set_xlim(0,RATE//2)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude")

def update_plot(frame):
    try:
        data=np.frombuffer(stream.read(CHUNK),dtype=np.int16)
        spectrum=np.abs(np.fft.fft(data))[:CHUNK//2] 
        line.set_ydata(spectrum)
    except OSError as e:
        print(f"Error updating plot: {e}")
    return line,
	
ani = FuncAnimation(fig, update_plot, blit=True)
#bliting=keeping used frames as background to reduce compute

try:
    plt.show()
except KeyboardInterrupt: 
    pass

try:    
    stream.stop_stream()
    stream.close()
    audio.terminate()
except OSError as e:
    print (f"Error closing audio stream: {e}")