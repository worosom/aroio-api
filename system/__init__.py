import os
from subprocess import run
from .lms import LMS
from .network import Network
from .card import Card

CHECKSOUNDCARD = 'checksoundcard'
HEARTBEAT_LED = 'echo heartbeat >/sys/class/leds/led0/trigger'
REBOOT = 'reboot -d 1 &'


class System:
    def __init__(self):
        self.network = Network()
        self.lms = LMS()
        self.card = Card()

    @property
    def has_input(self):
        return os.path.isfile('/proc/asound/card0/pcm0c')

    @property
    def has_bt(self):
        return os.path.isfile('/sys/class/bluetooth/hci0')

    def reboot(self):
        run(HEARTBEAT_LED)
        run(CHECKSOUNDCARD)
        run(REBOOT)
