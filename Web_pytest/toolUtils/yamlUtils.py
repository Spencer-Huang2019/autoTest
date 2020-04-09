import yaml

class Yaml(object):

    def __init__(self, filePath):
        self.filePath = filePath

    def readYaml(self):
        with open (self.filePath, 'r', encoding= "utf-8") as f:
            content = f.read()
            data = yaml.load(content, Loader=yaml.FullLoader)
        return data

if __name__ == '__main__':
    filepath = "../config/elementLoc/loginEle.yaml"
    r = Yaml(filepath)
    print(r.readYaml())