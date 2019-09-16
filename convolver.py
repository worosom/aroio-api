import os
from system.calls import Calls

FILTER_DIR = '/boot/filter'


class Convolver:
    def __init__(self, config):
        self.config = config

    @property
    def active_filter(self):
        return Calls.call('GET_FILTER')

    @active_filter.setter
    def active_filter(self, value):
        value = int(value)
        return Calls.run('SET_FILTER', f'0 {2*value} 1 {2*value + 1}')

    @property
    def volume(self):
        return Calls.call('GET_VOLUME')

    @volume.setter
    def volume(self, value):
        return Calls.run('SET_VOLUME', value)

    def get_filter_choices(self):
        try:
            rate = str(int(self.config['rate']) // 1000)
            files = [f for f in os.listdir(FILTER_DIR) if f.endswith('.dbl')]
            names = [f.split('.')[0] for f in files]
            names = [n[:len(n)-len(rate)-1] for n in names if n.endswith(rate)]
            names = list(set(names))
            return names
        except Exception as e:
            print(e)
