from django.shortcuts import render_to_response

"""
返回页面
"""


# 首页
def index(request):
    return render_to_response('index.html')


# 用例集
def suite(request):
    return render_to_response('suite.html')


# 用例
def case(request):
    try:
        suiteid = request.GET.get('suiteid')
    except:
        suiteid = False
    try:
        modularid = request.GET.get('modularid')
    except:
        modularid = False
    return render_to_response('case.html', {'suiteid': suiteid, 'modularid': modularid})


# 用例报告
def case_report(request):
    return render_to_response('case_report.html')


# 用例集报告
def suite_report(request):
    return render_to_response('suite_report.html')


# 模块
def modular(request):
    return render_to_response('modular.html')
