```python
import pyttsx3

class TTSSystem:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, response):
        self.engine.say(response)
        self.engine.runAndWait()

if __name__ == "__main__":
    tts = TTSSystem()
    tts.speak("Hello, I am K.A.R.A.")
```