from .yamlUtils import Yaml

filePath = "./config/configFile.yaml"
class Conf(object):
    def __init__(self, file = filePath):
        self.filepath = file

    def read(self):
        confData = Yaml(self.filepath).readYaml()
        return confData

