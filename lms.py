from .calls import Calls


class LMS:
    def restart(self):
        Calls.run('RESTART_LMS')
