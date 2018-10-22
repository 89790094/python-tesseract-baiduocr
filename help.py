import requests
import re
import os
import jieba


def fetchRemoteImg(url):
    local = re.sub(r'^(http|https)://.*\.(com|cn)', '', url)
    dir = os.getcwd() + os.path.dirname(local)
    if not os.path.exists(dir): os.makedirs(dir, exist_ok=True)
    fn = os.path.join(dir, os.path.basename(local))
    if os.path.exists(fn):
        return fn
    else:
        img = requests.get(url, verify=False)
        with open(fn, 'wb') as file:
            file.write(img.content)
            file.flush()
            os.fsync(file.fileno())
        if os.path.isfile(fn):
            return fn
        else:
            return


def fetchImgUrl(str):
    urls = []
    for url in re.findall(r'src="(.*?)"', str):
        urls.append(fetchRemoteImg(url) if re.match(r'^(http|https)://.*\.(com|cn)', url) else fetchRemoteImg('https://8jieke.com' + url))
    return urls
