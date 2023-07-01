```python
import pvporcupine
import pyaudio
import struct

class WakeWordDetector:
    def __init__(self, wake_word="KARA"):
        self.wake_word = wake_word
        self.porcupine = None
        self.pa = None
        self.audio_stream = None

    def initialize(self):
        try:
            self.porcupine = pvporcupine.create(keywords=[self.wake_word])
            self.pa = pyaudio.PyAudio()

            self.audio_stream = self.pa.open(
                rate=self.porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.porcupine.frame_length,
                input_device_index=None)

        except Exception as e:
            print(f"Failed to initialize Porcupine: {e}")

    def listen(self):
        if not self.porcupine or not self.audio_stream:
            print("Porcupine not initialized")
            return

        while True:
            pcm = self.audio_stream.read(self.porcupine.frame_length)
            pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)

            result = self.porcupine.process(pcm)

            if result >= 0:
                print(f"Wake word detected: {self.porcupine.keywords[result]}")
                break

    def close(self):
        if self.audio_stream is not None:
            self.audio_stream.close()

        if self.pa is not None:
            self.pa.terminate()

        if self.porcupine is not None:
            self.porcupine.delete()

if __name__ == "__main__":
    detector = WakeWordDetector()
    detector.initialize()
    detector.listen()
    detector.close()
```