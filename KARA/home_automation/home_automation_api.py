```python
import homeassistant as ha

class HomeAutomationAPI:
    def __init__(self):
        self.ha_api = ha.API('localhost', 'your_password')

    def execute(self, command):
        device, action = self.parse_command(command)
        if action == 'turn on':
            self.ha_api.turn_on(device)
        elif action == 'turn off':
            self.ha_api.turn_off(device)
        elif action == 'set temperature':
            self.ha_api.set_temperature(device, command['temperature'])
        else:
            print(f"Unknown command: {command}")

    def parse_command(self, command):
        # This is a simple command parser. You might need to replace it with a more sophisticated one.
        words = command.split()
        device = words[0]
        action = ' '.join(words[1:])
        return device, action
```