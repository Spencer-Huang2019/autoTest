import os
from os import path
import sys

d = path.dirname(__file__)
parent_path = os.path.dirname(d)
sys.path.append(parent_path)

from project.toolUtils.logUtils import log
import json
import requests

logfile = "./logFile/loginApi_log.txt"
logger = log(logfile)

class loginApi(object):
    def __init__(self, url, method, headers, payload):
        self.url = url
        self.method = method
        self.headers = json.loads(headers)
        self.payload = json.loads(payload)

    def request(self):
        # logger.msg("[url:%s headers:%s payload:%s]" % (self.url,self.headers,self.payload),"info")
        if self.method.upper() == "POST":
            if self.headers == "":
                res = requests.post(self.url, data=json.dumps(self.payload))
            else:
                res = requests.post(self.url, headers=self.headers, data=json.dumps(self.payload))

        if self.method.upper() == "GET":
            res = requests.get(self.url, headers=self.headers, params=self.payload)
        # logger.msg("statusCode: %d" % res.status_code, "info")
        return res
