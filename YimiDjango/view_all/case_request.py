from django.http import HttpResponse
import json
from YimiDjango.ussd.case import case_main

'''
用例页面接口
'''


# 返回列表查询数据
def get_case_data(request):
    data = case_main.get_case_select(request.POST)
    return HttpResponse(json.dumps({"aaData": data}))
