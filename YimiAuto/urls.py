"""YimiAuto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from YimiDjango.view_all import page, case_report_request, case_request, modular_request, suite_report_request, \
    suite_request

urlpatterns = [
    path('admin/', admin.site.urls),

    # 页面
    path('', page.index, name='index'),
    path('suite.html/', page.suite, name='suite'),
    path('case.html/', page.case, name='case'),
    path('case_report.html/', page.case_report, name='suite'),
    path('suite_report.html/', page.suite_report, name='suite'),
    path('modular.html/', page.modular, name='suite'),

    # 接口
    path('casedata', case_request.get_case_data),
    path('suitedata', suite_request.get_suite_data),
    path('get_suite_details', suite_request.get_suite_details)
]
