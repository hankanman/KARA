```python
import sys
sys.path.append('KARA')

from wake_word_detection import porcupine
from speech_recognition import whisper_asr
from natural_language_processing import gpt_api
from text_to_speech_synthesis import tts_system
from home_automation import home_automation_api
from continuous_learning import learning_module

def initialize():
    porcupine.initialize()
    whisper_asr.initialize()
    gpt_api.initialize()
    tts_system.initialize()
    home_automation_api.initialize()
    learning_module.initialize()

def main():
    initialize()
    wake_word = "Hey Kara"
    while True:
        if porcupine.listen(wake_word):
            user_command = whisper_asr.listen()
            processed_command = gpt_api.process(user_command)
            response = home_automation_api.execute(processed_command)
            tts_system.speak(response)
            learning_module.learn(user_command, response)

if __name__ == "__main__":
    main()
```