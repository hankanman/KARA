```python
import pvporcupine
import pyaudio
import struct

class WakeWordDetector:
    def __init__(self, wake_word="hey kara"):
        self.wake_word = wake_word
        self.porcupine = None
        self.pa = None
        self.audio_stream = None

    def __enter__(self):
        self.porcupine = pvporcupine.create(keywords=[self.wake_word])
        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length,
            input_device_index=None)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.audio_stream is not None:
            self.audio_stream.close()
        if self.pa is not None:
            self.pa.terminate()
        if self.porcupine is not None:
            self.porcupine.delete()

    def detect_wake_word(self):
        while True:
            pcm = self.audio_stream.read(self.porcupine.frame_length)
            pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
            result = self.porcupine.process(pcm)
            if result >= 0:
                return True
        return False

if __name__ == "__main__":
    with WakeWordDetector() as detector:
        if detector.detect_wake_word():
            print("Wake word detected!")
```
