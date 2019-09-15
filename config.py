import configparser

CONFIG_PATH = 'userconfig.txt'


class Config:
    def __init__(self, system):
        self.system = system
        self.parser = configparser.ConfigParser()
        self.load()

    def load(self):
        with open(CONFIG_PATH, 'r') as f:
            config_string = '[DEFAULT]\n' + f.read()
        self.parser.read_string(config_string)
        self.config = self.parser['DEFAULT']
        for key in self.config:
            self.config[key] = self.config[key].strip('"')

    def save(self, _config):
        with self.system.card:
            with open(CONFIG_PATH, 'w') as f:
                for key in _config.keys():
                    self.config[key] = str(_config[key])
                    f.write(f'{key.upper()}="{self.config[key]}"\n')

    def __dict__(self):
        return dict(self.config)

    def __getitem__(self, key):
        return self.config[key]
