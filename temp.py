"""
此方式为临时API接口方式，仅供内部使用，不要对外！
v1.1版本，修复无法发送数据问题
"""


import json
import os

import requests

import time

pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep


def parseUserInfo():
    allUsers = []
    for file_name in os.listdir('.'):
        if file_name.endswith('.json'):
            with open(file_name, encoding="utf-8") as f:
                data = json.load(f)
                allUsers.extend(data)

    return allUsers


if __name__ == '__main__':
    users = parseUserInfo()

    for user in users:
        time.sleep(1)
        print('已加载用户 ' + user['alias'])
        headers = {
            'Auth': 'b1c2',
            "content-type": "application/json;charset=UTF-8"
        }
        resp = requests.post('http://api.sandbox.sxba.xuanran.cc', headers=headers,
                             data=json.dumps(user).encode('utf-8'))

        res = resp.json()
        if res['code'] == 20000:
            print(user['alias'] + ' 打卡成功！')
            continue
        print(user['alias'] + ' 打卡失败！错误原因：' + res['message'])
