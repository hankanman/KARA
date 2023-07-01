```python
import openai

class NaturalLanguageProcessing:
    def __init__(self):
        self.gpt = openai.GPT()

    def process_text(self, text):
        response = self.gpt.complete(prompt=text, max_tokens=60)
        return response.choices[0].text.strip()

def process_command(command):
    nlp = NaturalLanguageProcessing()
    response = nlp.process_text(command)
    return response
```