import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

class AudioRecorder:
    def __init__(self, buffer):
        self.buffer = buffer
        self.recording = False
        self.buffer_full = False
        self.fs = 44100  # Sample rate
        self.seconds = 5  # Duration of recording
        self.myrecording = np.array([])

    def record(self):
        while True:
            if self.recording:
                # Record audio for the given number of seconds
                temp_recording = sd.rec(int(self.seconds * self.fs), samplerate=self.fs, channels=2)
                sd.wait()  # Wait until recording is finished
                self.myrecording = np.append(self.myrecording, temp_recording)  # Append to the existing recording

                # Check if the buffer is full
                if self.myrecording.nbytes > len(self.buffer):
                    self.buffer_full = True

    def start_recording(self):
        print("Recording...")
        self.recording = True

    def stop_recording(self):
        print("Stopped recording")
        self.recording = False
        # Write the recording to a WAV file
        write('output.wav', self.fs, self.myrecording)
        self.myrecording = np.array([])  # Clear the recording

    def rotate_buffer(self):
        # Remove the oldest data from the buffer to make room for new data
        self.myrecording = self.myrecording[-int(self.fs * self.seconds):]
        self.buffer_full = False

    def reset(self):
        self.recording = False
        self.buffer_full = False
        self.myrecording = np.array([])
