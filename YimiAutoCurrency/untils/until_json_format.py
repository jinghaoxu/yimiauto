# 格式化json字符串
def json_gsh(data):
    enter = '\n'  # 回车字符串
    ksp = '    '  # 空格
    res = ''
    k = 0
    data = str(data)
    for i in range(len(data)):
        ele = data[i]
        if ele == '{' or ele == '[':
            ele = ele + enter
            k = k + 1
            for ii in range(k):
                ele = ele + ksp
        elif ele == '}' or ele == ']':
            k = k - 1
            for ii in range(k):
                ele = ksp + ele
            ele = enter + ele
        elif ele == ',':
            ele = ele + enter
            for ii in range(k):
                ele = ele + ksp
        elif ele == ':':
            ele = ele + ''
        res = res + ele
    return res


if __name__ == '__main__':
    a = {'1': '2', '3': '4'}
    print(json_gsh(a))
