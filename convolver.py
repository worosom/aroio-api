import os
from subprocess import run, check_output

GET_FILTER = '/usr/bin/controlbrutefir getFilter'
SET_FILTER = '/usr/bin/controlbrutefir chgFilter'

FILTER_DIR = './filter'


class Convolver:
    def __init__(self, config):
        self.config = config

    @property
    def active_filter(self):
        try:
            ret = check_output(GET_FILTER, shell=True).decode('UTF-8')
            return int(ret.split(':')[-1])//2
        except Exception as e:
            print(e)

    @active_filter.setter
    def set_filter(self, value):
        cmd = f'{SET_FILTER} {0} {2*value} {1} {2*value + 1}'
        try:
            run(cmd)
        except Exception as e:
            print(e)

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
