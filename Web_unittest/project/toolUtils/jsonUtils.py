import json

class Json(object):

    def __init__(self, filePath):
        self.filePath = filePath

    def readJson(self):
        with open(self.filePath, 'r', encoding="utf-8") as f:
            data = json.loads(f.read())
            return data

if __name__ == '__main__':
    filePath = "../data/loginTC.json"
    j = Json(filePath)
    content = j.readJson()
    print(content)
    print(type(content))