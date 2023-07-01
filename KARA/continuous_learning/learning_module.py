```python
import os
import json

class LearningModule:
    def __init__(self):
        self.data_path = "data/user_interactions.json"
        self.interactions = self.load_interactions()

    def load_interactions(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_interactions(self):
        with open(self.data_path, 'w') as file:
            json.dump(self.interactions, file)

    def learn(self, user_command, response):
        interaction = {
            "user_command": user_command,
            "response": response
        }
        self.interactions.append(interaction)
        self.save_interactions()

    def get_learned_response(self, user_command):
        for interaction in self.interactions:
            if interaction["user_command"] == user_command:
                return interaction["response"]
        return None
```