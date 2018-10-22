from aip import AipOcr
import re
import os

from help import fetchRemoteImg

config = ('14401465', 'kIQ9vSXl0ibjMoiUuRDElnLC', 'Wm3k8jLCSBm1UkFAZPQgLvkrse2adVFU')
ID, KEY, SECRET = config
client = AipOcr(ID, KEY, SECRET)


def readImg(path):
    with open(path, 'rb') as fp:
        return fp.read()

def baiduOcr(url):
    fn = url if not re.search(r'^(http|https)://', url) else fetchRemoteImg(url)
    if os.path.isfile(fn) and os.path.exists(fn):
        img = readImg(fn)
        result = client.basicGeneral(img)
        return ''.join([v['words'] for v in result['words_result']]) if 'words_result' in result else ''
    else:
        return


if __name__ == '__main__':
    print(baiduOcr('http://www.zmonster.me/assets/img/ocr_test_003.jpg'))
