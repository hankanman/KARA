```python
import pyttsx3

class TextToSpeechSynthesizer:
    def __init__(self):
        self.engine = pyttsx3.init()

    def synthesize_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    tts = TextToSpeechSynthesizer()
    tts.synthesize_speech("Hello, I am K.A.R.A. your residential assistant.")
```