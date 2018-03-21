"""
图灵机器人
"""
import requests
import json
from YimiAutoCurrency.untils.until_json_format import json_gsh


def request(data):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
    }
    a = requests.post(data['url'], json.dumps(data['data']), headers=headers)
    print(json_gsh(a.text))


tuling = {
    'url': 'http://www.tuling123.com/openapi/api',
    'data': {
        'key': '83ef256ee52949358ea30c4f5bcfddd9',
        'info': '千万人 用英语怎么说',
        'userid': '66'
    }
}
if __name__ == '__main__':
    request(tuling)
