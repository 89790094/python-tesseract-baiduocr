from PIL import Image, ImageEnhance
import pytesseract
import os

from help import fetchRemoteImg


def advanced(image_path, lang='chi_sim+eng+equ', mode='-psm 3'):
    if os.path.isfile(image_path):
        img = Image.open(image_path)
        '''图像前期处理'''
        # contrast = ImageEnhance.Contrast(img).enhance(2.0)
        ocrImg = ImageEnhance.Brightness(img).enhance(0.5)
        return pytesseract.image_to_string(ocrImg, lang, mode)
    else:
        return


def general(img, lang='chi_sim+eng+equ', mode='-psm 3'):
    if os.path.isfile(img):
        return pytesseract.image_to_string(Image.open(img), lang, mode)
    else:
        return


if __name__ == '__main__':
    fn = fetchRemoteImg('https://www.8jieke.com/upload/image/20170518/1495107410191608.png')
    print(general(fn))
    # print(imgToStr('2.png'))
