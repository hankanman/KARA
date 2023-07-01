```python
import homeassistant as ha

class HomeAutomation:
    def __init__(self):
        self.ha_api = ha.API()

    def control_light(self, light_id, state):
        if state.lower() == "on":
            self.ha_api.turn_on(light_id)
        elif state.lower() == "off":
            self.ha_api.turn_off(light_id)
        else:
            print("Invalid state. Please specify 'on' or 'off'.")

    def adjust_thermostat(self, thermostat_id, temperature):
        self.ha_api.set_temperature(thermostat_id, temperature)

    def play_music(self, music_id):
        self.ha_api.play_media(music_id)

def control_home_devices(device, action, parameters):
    home_automation = HomeAutomation()

    if device.lower() == "light":
        home_automation.control_light(parameters["light_id"], action)
    elif device.lower() == "thermostat":
        home_automation.adjust_thermostat(parameters["thermostat_id"], action)
    elif device.lower() == "music":
        home_automation.play_music(parameters["music_id"])
    else:
        print("Invalid device. Please specify 'light', 'thermostat', or 'music'.")
```