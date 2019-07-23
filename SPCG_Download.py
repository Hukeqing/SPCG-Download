import common
import os
import time

mode = 0
sleeptime = 3
first = 1
end = common.lenth + 1
maxphoto = 395
photoperpage = 40
maxpage = 10
print('******************************************************************')
print('Create by Mauve')
print('我的GitHub：https://github.com/Hukeqing')
print('我的bilibili：https://space.bilibili.com/175413312')
print()
print('所有的CG仅用于交流，学习和分享，')
print('严禁未经官方授权的任何商业用途，')
print('若因此引起的版权纠纷，本人不对所造成的后果负责。')
print('******************************************************************')
print()
try:
    mode = int(input('请输入需要的下载方式\n1、全部下载\n2、按页下载\n3、区间下载\n请输入编号并按下回车：'))
except ValueError:
    print('错误!不是数字，程序终止')
    time.sleep(sleeptime)
    exit(0)
if mode < 1 or mode > 3:
    print('错误，超出范围，程序终止')
    time.sleep(sleeptime)
    exit(0)
savepath = input('请输入文件保存的地址，按下回车确定(留空则保存到当前目录下)：')
if savepath == "":
    savepath = os.path.abspath(".")

if not os.path.isdir(savepath):
    print('这不是一个目录，程序终止！')
    time.sleep(sleeptime)
    exit(0)

if mode == 1:
    first = 1
    end = common.lenth + 1
elif mode == 2:
    pages = 0
    try:
        pages = int(input('请输入要下载的页码（仅数字，一个整数，每一页默认下载40个图片）\n例如第一页下载 1 - ' + str(photoperpage) + ' 的图片'))
    except ValueError:
        print('错误！不是数字，程序终止')
        time.sleep(sleeptime)
        exit(0)
    if pages < 0 or pages > maxpage:
        print('错误！超出范围，程序终止')
        time.sleep(sleeptime)
        exit(0)
    first = pages * photoperpage + 1
    end = first + photoperpage - 1
else:
    try:
        first = int(input('请输入要下载的起始编号（1-' + str(maxphoto) + '）：'))
    except ValueError:
        print('错误！不是数字，程序终止')
        time.sleep(sleeptime)
        exit(0)
    if first < 0 or first > maxphoto:
        print('错误！超出范围，程序终止')
        time.sleep(sleeptime)
        exit(0)
    try:
        end = int(input('请输入要下载的结束编号（' + str(first) + '-' + str(maxphoto) + '）：'))
    except ValueError:
        print('错误！不是数字，程序终止')
        time.sleep(sleeptime)
        exit(0)
    if end < first or end > maxphoto:
        print('错误！超出范围，程序终止')
        time.sleep(sleeptime)
        exit(0)

while first <= end:
    print('正在下载第' + str(first) + '张CG图片')
    if first == 386 or first == 387:
        print('正在下载被和谐的图片，下载速度较慢')
    common.download(first, savepath)
    time.sleep(0.1)
    first += 1
print('下载完成！')
time.sleep(sleeptime)
