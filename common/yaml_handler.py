# -*- coding: UTF-8 -*-
import yaml
import os


class YamlHandler:
    def __init__(self, file):
        self.file = file

    def read_yaml(self, encoding='utf-8'):
        with open(self.file, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def write_yaml(self, data, encoding='utf-8'):
        with open(self.file, encoding=encoding, mode='w') as f:
            return yaml.dump(data, stream=f, allow_unicode=True)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
yaml_data = YamlHandler(base_dir + '/config/application.yaml').read_yaml()