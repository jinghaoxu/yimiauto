def isnull(par, name, dictt):
    try:
        idd = par[name]
        dictt.append(par[name])
    except:
        idd = '%'
    return idd, dictt


def addif(idd, strr):
    if idd != '%':
        return strr
    else:
        return ' '