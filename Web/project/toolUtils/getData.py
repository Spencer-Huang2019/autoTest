from project.toolUtils.jsonUtils import Json

class GetData(Json):

    def getAll(self):
        values = []
        for case in self.readJson():
            values.append(tuple(list(case.values())[:4]))
        return values

    def configFile(self):
        allData = self.getAll()
        config = allData.pop(0)[0]
        self.data = allData
        return config

    def testData(self):
        return self.data


if __name__ == '__main__':
    filepath = "../data/loginTC.json"
    # getObj = getData(filepath, "login",0, 5)
    # print(getObj.data())
    dataDict = [{'id': '1', 'desc': 'login success', 'data': {'username': '15122888806', 'password': 'huanhuan350881'}, 'expected': '', 'preId': None}, {'id': '2', 'desc': 'logout success', 'data': {'username': '15122888806', 'password': 'huanhuan350881'}, 'expected': '', 'preId': '1'}]
    get = GetData(filepath)
    print(get.configFile())
    print(get.testData())