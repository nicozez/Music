
import tkinter as tk
from tkinter import ttk
import numpy as np
import pyaudio

def play_sound(frequency, amplitude):
    p = pyaudio.PyAudio()
    volume = amplitude
    fs = 44100  # sampling rate, Hz, int
    duration = 1.0   # in seconds, float
    f = frequency  # sine frequency, Hz, float

     
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

  
    stream.write(volume * samples)

    stream.stop_stream()
    stream.close()

    p.terminate()

# GUI 
def create_gui():
    def update_sound(val):
        frequency = float(frequency_slider.get())
        amplitude = float(amplitude_slider.get())
        play_sound(frequency, amplitude)

    root = tk.Tk()
    root.title("Sound Modulator")

    mainframe = ttk.Frame(root, padding="10 10 20 20")
    mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    # Frequency 
    frequency_slider = tk.Scale(mainframe, from_=100, to=2000, orient=tk.HORIZONTAL, label="Frequency (Hz)")
    frequency_slider.grid(column=1, row=1, sticky=(tk.W, tk.E))
    frequency_slider.set(440)
    # Amplitude
    amplitude_slider = tk.Scale(mainframe, from_=0.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, label="Amplitude")
    amplitude_slider.grid(column=1, row=2, sticky=(tk.W, tk.E))
    amplitude_slider.set(0.5)
    # Update 
    update_button = ttk.Button(mainframe, text="Play Sound", command=lambda: update_sound(None))
    update_button.grid(column=1, row=3, sticky=(tk.W, tk.E))

    root.mainloop()

if __name__ == "__main__":
    create_gui()



