import tkinter
import tkinter.messagebox
import tkinter.ttk
import tkinter.filedialog
import common
import time


def showpl():
    try:
        page = int(et.get())
    except ValueError:
        tkinter.messagebox.showerror('错误', '输入的不是数字')
        et.delete(0)
        return
    common.showinweb(page)


def changemode(x):
    downloadmain.pack_forget()
    if downloadtuble.index(downloadcb.get()) == 1:
        downloadmode2.pack_forget()
        downloadmode3.pack_forget()
        downloadmode1.pack()
    elif downloadtuble.index(downloadcb.get()) == 2:
        downloadmode1.pack_forget()
        downloadmode3.pack_forget()
        downloadmode2.pack()
    elif downloadtuble.index(downloadcb.get()) == 3:
        downloadmode1.pack_forget()
        downloadmode2.pack_forget()
        downloadmode3.pack()
    if downloadtuble.index(downloadcb.get()) != 0:
        downloadmain.pack()


def download():
    if downloadtuble.index(downloadcb.get()) == 1:
        section = common.downloadmode1()
    elif downloadtuble.index(downloadcb.get()) == 2:
        section = common.downloadmode2(downloadmode2en.get())
    elif downloadtuble.index(downloadcb.get()) == 3:
        section = common.downloadmode3(downloadmode3en1.get(), downloadmode3en2.get())
    else:
        return
    if section == -1:
        tkinter.messagebox.showerror('错误', '输入的不是数字')
        return
    elif section == 999:
        tkinter.messagebox.showerror('错误', '数字范围有误')
        return
    downloadpath = tkinter.filedialog.askdirectory(title='保存路径')
    downloadlogstr.set('开始下载')
    for i in range(section[0], section[1] + 1):
        downloadlogstr.set('正在下载第' + str(i) + '张CG图片')
        if i == 386 or i == 387:
            downloadlogstr.set('正在下载被和谐的图片，下载速度较慢')
        window.update()
        common.download(i, downloadpath)
        time.sleep(0.1)
    downloadlogstr.set('下载完成')
    tkinter.messagebox.showinfo('提示', '下载完成')


window = tkinter.Tk()
window.title('Summer Pockets CG资源下载器GUI版')
window.geometry('500x500')
window.iconbitmap(common.resource_path('SummerPockets.ico'))
# 预览模块
showpla = tkinter.Label(window, text='图片预览功能', font=('Arial', 20), width=100, height=2)
showpla2 = tkinter.Label(window, text='请在下方输入一个数字(图片编号)，然后点击"预览"按钮', font=('Arial', 12))
et = tkinter.Entry(window, relief='sunken', bd=5)
showmainbutton = tkinter.Button(window, text='预览', bg='blue', font=('Arial', 20), width=10, height=2, command=showpl)
showpla.pack()
showpla2.pack()
et.pack()
showmainbutton.pack()
l = tkinter.Label(window,
                  text='-----------------------------------------------------------------------------------------------------------------')
l.pack()
# 下载模块
downloadla = tkinter.Label(window, text='下载功能', font=('Arial', 20), width=100, height=2)
downloadla.pack()
downloadmode = tkinter.StringVar()
downloadtuble = ('-请选择-', '全部下载', '按页下载', '区间下载')
downloadcb = tkinter.ttk.Combobox(window, textvariable=downloadmode)
downloadcb['value'] = downloadtuble
downloadcb.current(0)
downloadcb.bind("<<ComboboxSelected>>", changemode)
downloadcb.pack()
# 下载模块1——全部下载
downloadmode1 = tkinter.Frame(window)
downloadmode1la = tkinter.Label(downloadmode1, text='下载全部的CG，共' + str(common.lenth) + '张', font=('Arial', 20),
                                width=100, height=2, bg='yellow')
downloadmode1la.pack()
# 下载模块2——按页下载
downloadmode2 = tkinter.Frame(window)
downloadmode2en = tkinter.Entry(downloadmode2, relief='sunken', bd=5, width=10)
downloadmode2la1 = tkinter.Label(downloadmode2, text='第', bd=5)
downloadmode2la2 = tkinter.Label(downloadmode2, text='页', bd=5)
downloadmode2la1.pack(side='left')
downloadmode2en.pack(side='left')
downloadmode2la2.pack(side='left')
# 下载模式3——区间下载
downloadmode3 = tkinter.Frame(window)
downloadmode3en1 = tkinter.Entry(downloadmode3, relief='sunken', bd=5, width=10)
downloadmode3la1 = tkinter.Label(downloadmode3, text='第', bd=5)
downloadmode3la2 = tkinter.Label(downloadmode3, text='张至第', bd=5)
downloadmode3en2 = tkinter.Entry(downloadmode3, relief='sunken', bd=5, width=10)
downloadmode3la3 = tkinter.Label(downloadmode3, text='张CG', bd=5)
downloadmode3la1.pack(side='left')
downloadmode3en1.pack(side='left')
downloadmode3la2.pack(side='left')
downloadmode3en2.pack(side='left')
downloadmode3la3.pack(side='left')
# 下载通用
downloadmain = tkinter.Frame(window)
downloadmainbutton = tkinter.Button(downloadmain, text='确定下载', font=('Arial', 20), bg='red', width=10, height=2,
                                    command=download)
downloadlogstr = tkinter.StringVar()
downloadlog = tkinter.Label(downloadmain, textvariable=downloadlogstr)
downloadmainbutton.pack()
downloadlog.pack()
# 打包GUI
window.mainloop()
