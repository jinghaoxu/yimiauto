from YimiAutoCurrency.untils import until_sqllite3 as us
from YimiDjango.ussd.suite import suiteRm
from YimiDjango.ussd.suite import suiteWm


def get_suite_select(data):
    return us.sqlite_select(suiteRm.select, data)


def get_suite_details(data):
    return us.sqlite_select(suiteRm.suite_details, data)


if __name__ == '__main__':
    print(get_suite_select([]))
