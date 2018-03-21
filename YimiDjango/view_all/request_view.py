from django.http import HttpResponse
import json

from YimiDjango.ussd.suite import suite_main
from YimiDjango.ussd.case import case_main


def get_suite_data(e):
    data = suite_main.get_suite_select(e)
    return HttpResponse(json.dumps({"aaData": data}))


def get_suite_details(dataa):
    data = suite_main.get_suite_details(dataa)
    for i in data:
        if i['status'] == '0':
            i['status'] = '否'
        else:
            i['status'] = '是'
    return HttpResponse(json.dumps({"aaData": data}))


def get_case_data(get):
    data = case_main.get_case_default(get)
    return HttpResponse(json.dumps({"aaData": data}))


if __name__ == '__main__':
    get_suite_details(1)
