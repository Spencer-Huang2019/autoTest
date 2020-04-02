import requests
import json
from project.toolUtils.logUtils import log

logfile = "./logFile/registryApi_log.txt"
logger = log(logfile)

class apiUtils(object):

    def apiVisit(url, method, headers, payload):
        res = None
        # logger.msg("request apiVisit", "info")
        if method.upper() == "POST":
            # logger.msg("post method", "info")
            if headers == "":
                res = requests.post(url, data=json.dumps(payload))
            else:
                res = requests.post(url, headers=json.loads(headers), data=json.dumps(payload))

        if method.upper() == "GET":
            res = requests.get(url, headers=json.loads(headers), params=payload)
        # logger.msg("statusCode: %d" % res.status_code, "info")
        return res

if __name__ == '__main__':
    res = apiVisit("http://localhost:8899/spencer/api/login", "post",payload={"userName": "Alex zhao", "password": "12345"})
    print(res.json())
    print(res.status_code)