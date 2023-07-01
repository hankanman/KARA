```python
import openai

class SpeechRecognition:
    def __init__(self):
        self.asr_api = openai.WhisperASR()

    def convert_speech_to_text(self, audio_input):
        try:
            response = self.asr_api.transcribe(audio_input)
            return response['text']
        except Exception as e:
            print(f"Error in converting speech to text: {str(e)}")
            return None

if __name__ == "__main__":
    sr = SpeechRecognition()
    audio_input = "audio_file.wav"  # This should be the path to the audio file
    text = sr.convert_speech_to_text(audio_input)
    if text:
        print(f"Converted text: {text}")
    else:
        print("Failed to convert speech to text.")
```
