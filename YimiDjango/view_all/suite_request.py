from django.http import HttpResponse
import json
from YimiDjango.ussd.suite import suite_main

'''
用例集页面接口
'''


# 返回用例集列表查询数据
def get_suite_data(request):
    suitename = '%' + request.POST['suitename'] + '%'
    suitemodular = '%' + request.POST['suitemodular'] + '%'
    data = suite_main.get_suite_select([suitename, suitemodular])
    return HttpResponse(json.dumps({"aaData": data}))


# 返回详情列表数据
def get_suite_details(request):
    data = suite_main.get_suite_details([request.POST.get('nums')])
    for i in data:
        if i['status'] == '0':
            i['status'] = '否'
        else:
            i['status'] = '是'
    return HttpResponse(json.dumps({"aaData": data}))
