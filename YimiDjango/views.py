# Create your views here.
from YimiDjango.view_all import page
from YimiDjango.view_all import request_view
import json


def index(request):
    return page.index()


def suite(request):
    return page.suite(request)


def case(request):
    return page.case(request)


def case_report(request):
    return page.case_report(request)


def suite_report(request):
    return page.suite_report(request)


def modular(request):
    return page.modular(request)


###################

def suitedata(request):
    suitename = '%' + request.POST['suitename'] + '%'
    suitemodular = '%' + request.POST['suitemodular'] + '%'
    return request_view.get_suite_data([suitename, suitemodular])


def get_suite_details(request):
    return request_view.get_suite_details([request.POST.get('nums')])


def casedata(request):
    return request_view.get_case_data(request.GET)
