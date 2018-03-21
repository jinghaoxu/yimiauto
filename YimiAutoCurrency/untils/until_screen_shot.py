"""
1、截屏，存储到指定路径
2、创建时间：2017-11-22
3、创建人：徐敬浩
"""
from PIL import ImageGrab
from YimiAutoCurrency.constants import object_path
import time


# 两个参数：name：截屏的图的文件名，存放在指定的地方，bbox：截屏的大小=(100,100,100,100)
def pngshot(name, bbox=None):
    pngpath = object_path.OBJECTPATH + '/data/Screenshot/'
    pngname = str(name) + '_' + str(time.time()) + '.png'

    im = ImageGrab.grab(bbox=bbox)
    im.save(pngpath + pngname)


if __name__ == '__main__':
    pngshot('123')
