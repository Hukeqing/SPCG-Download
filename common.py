# -*- coding:utf-8 -*-
import os
import sys
import requests
import webbrowser


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


with open(resource_path('page.txt'), 'r') as f:
    linker = f.read()
    linker = linker.split('\n')
    lenth = len(linker)
photoperpage = 40


def judgeid(id):
    if 0 <= id < len(linker):
        return True
    return False


def download(id, path):
    if not judgeid(id - 1):
        return False
    if not os.path.isdir(path):
        os.makedirs(path)
    regets = requests.get(linker[id - 1])
    with open(os.path.join(path, str(id) + '.jpg'), 'wb') as f:
        f.write(regets.content)
    return True


def showinweb(id):
    if not judgeid(id - 1):
        return False
    webbrowser.open(linker[id - 1])
    return True


def downloadmode1():
    return (1, lenth)


def downloadmode2(page):
    try:
        first = (int(page) - 1) * 40 + 1
    except ValueError:
        return -1
    if int(page) > 10 or int(page) < 1:
        return 999
    last = first + 39
    return (first, last)


def downloadmode3(beg, end):
    try:
        first = int(beg)
        last = int(end)
    except ValueError:
        return -1
    if first > lenth or last > lenth or first < 1 or last < 1 or first > last:
        return 999
    return (first, last)


if __name__ == '__main__':
    showinweb(1)
