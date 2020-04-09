from toolUtils.jsonUtils import Json

class GetData(Json):

    def data(self):
        testData = self.readJson()["data"]

        data = []
        for item in testData:
            input = item["input"]
            expected = item["expected"]
            data.append([input, expected])
        return data

if __name__ == '__main__':
    filepath = "../caseData/dataLogin/dataPwSuc.json"
    # getObj = getData(filepath, "dataLogin",0, 5)
    # print(getObj.caseData())
    dataDict = [{'id': '1', 'desc': 'dataLogin success', 'caseData': {'username': '15122888806', 'password': 'huanhuan350881'}, 'expected': '', 'preId': None}, {'id': '2', 'desc': 'logout success', 'caseData': {'username': '15122888806', 'password': 'huanhuan350881'}, 'expected': '', 'preId': '1'}]
    data = GetData(filepath).data()
    print(data)
