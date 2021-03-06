import inspect


def props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not inspect.ismethod(value):
            pr[name] = value
    return pr


class API:
    def __init__(self, config):
        self.config = config

    def get_system_status(self):
        return {
            'network': self.get_network_status()
        }

    def get_network_status(self):
        return props(self.config.system.network)

    def get_iwlist(self):
        return self.config.system.network.iwlist()

    def search_update(self):
        return self.config.system.search_update(self.config['usebeta'])

    def get_log(self, log):
        return self.config.system.get_log(log)
