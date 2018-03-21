"""
返回一个字符串的MD5 编码
"""
import hashlib


# md5编码
def md5(data):
    formatt = hashlib.md5()  # 对字符串进行md5编码
    formatt.update(str(data).encode())  # 字符串需要进行编码（utf-8）
    return formatt.hexdigest()
