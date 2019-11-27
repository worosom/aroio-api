import os
from .lms import LMS
from .network import Network
from .card import Card
from .calls import Calls


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
        Calls.run('HEARTBEAT_LED')
        Calls.run('CHECKSOUNDCARD')
        Calls.run('REBOOT')

    def search_update(self, use_beta=False):
        if use_beta:
            return Calls.call('SEARCH_UPDATE_BETA')
        return Calls.call('SEARCH_UPDATE')

    def get_log(self, log):
        return Calls.call(f'{log}log'.upper())
