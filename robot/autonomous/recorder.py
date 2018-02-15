import wpilib
from magicbot import tunable
import json


class Recorder:
    """
    Record control input for playback as an autonomous mode.
    """
    directory = tunable('')
    recording_name = tunable('')

    frames = []

    def start(self, voltage):
        """
        Start a recording.

        :param voltage: Battery output voltage. Necessary for scaling speeds later on.
        """
        self.voltage = voltage

    def capture(self, joysticks):
        """
        Make snapshot of joystick inputs during this cycle.

        :param joysticks: List of joysticks to read.
        """
        data = {
            joysticks: []
        }
        for joystick in joysticks:
            data['joysticks'].append({
                'axes': [joystick.getRawAxis(axs) for axs in range(joystick.getAxisCount())],
                'buttons': [joystick.getRawButton(btn) for btn in range(joystick.getButtonCount())],
                'pov': [joystick.getPOV(pov) for pov in range(joystick.getPOVCount())],
            })
        self.frames.append(data)

    def stop(self):
        """
        End recording and save data to file.
        """
        data = {
            'voltage': self.voltage,
            'frames': self.frames,
        }
        with open(self.directory + '/' + self.recording_name, 'w+') as f:
            json.dump(data, f)

        self.voltage = None
        self.frames = []

    def execute(self):
        """
        Run periodically when injected through MagicBot.
        """
        pass
