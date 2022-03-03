import tkinter as tk
import tkinter.filedialog as tk_f
import requests
from aip import AipSpeech
from aip import AipImageClassify
from aip import AipOcr
import win32clipboard as w
import tkinter.messagebox
from PIL import Image, ImageTk

str1 = ''
str2 = ''
str3 = ''
str4 = ''
filename2 = ''
filename3 = ''
filename4 = ''
res1 = ''
res2 = ''
res3 = ''
res4 = ''
username = ''
password = ''
islogin = False
bgcolor = 'white'
fgcolor = 'black'
btbgcolor = 'white'


##############################################
def setText(str):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(str)
    w.CloseClipboard()


def translate(text):
    url = "http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i="
    response = requests.post(url + text)
    return response.json()


def gettsres(str):
    tsres = ''
    for str in translate(str)['translateResult'][-1]:
        tsres += str['tgt']
    return tsres


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def yuyin_str(file):
    APP_ID = '25040252'
    API_KEY = 'N3WI67KfM97Ap1KTZiEeyp66'
    SECRET_KEY = 'eLyw3N1pa1Qmdv7ZGYSDmgRXDLWoriLh'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    res = client.asr(get_file_content(file), 'm4a', 16000, {
        'dev_pid': 1537,
    })
    resstr = ''
    for str in res['result']:
        resstr += str
    return resstr


def pic_str1(file):
    APP_ID = '25332754'
    API_KEY = 'GLdKSKqruDf6q5mG0ZpgqHWS'
    SECRET_KEY = 'r79vgVoWIY04XAVszfb0BhDIDpjpCDGZ'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content(file)
    options = {"language_type": "CHN_ENG", "detect_direction": "true", "detect_language": "true"}
    res = client.basicGeneral(image, options)
    resstr = ''
    for str in res['words_result']:
        resstr += str['words']
    return resstr


def pic_str2(file):
    APP_ID = '25331649'
    API_KEY = 'WxnxY1W88IQZM0va57INtjj9'
    SECRET_KEY = 'sPojaBfbc2dd7FgAd1LGpmIW5GQqkbkW'
    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
    options = {"top_num": 1, "baike_num": 0}
    image = get_file_content(file)
    res = client.plantDetect(image, options)
    return res['result'][0]['name']


##############################################4个翻译  11111111

def btn1():
    cv1.place(x=-5, y=-5)
    cv2.place(x=66666, y=66666)
    cv2.place(x=66666, y=66666)
    cv3.place(x=66666, y=66666)
    cv_dibu.place(x=272, y=752)
    b_dibu2.config(relief='solid')
    b_dibu3.config(relief='solid')
    b_dibu4.config(relief='solid')
    b_dibu1.config(relief='flat')


def btn1_exit():
    cv1.place(x=66666, y=66666)
    cv_dibu.place(x=66666, y=66666)


def btn11():
    global str1
    global res1
    str1 = input1.get()
    if str1 == '':
        tk.messagebox.showinfo('提示', '输入不能为空')
        return
    res1show.delete('1.0', 'end')
    res1 = gettsres(str1)
    res1show.insert('end', res1)


def btn1_clear():
    varstr1.set('')  # input1 清空
    res1show.delete('1.0', 'end')


def jqb1():
    setText(res1)


##############################################4个翻译  2222222222


def btn2():
    cv2.place(x=-5, y=-5)
    cv1.place(x=66666, y=66666)
    cv3.place(x=66666, y=66666)
    cv4.place(x=66666, y=66666)
    cv_dibu.place(x=272, y=752)
    b_dibu1.config(relief='solid')
    b_dibu3.config(relief='solid')
    b_dibu4.config(relief='solid')
    b_dibu2.config(relief='flat')


def btn2_exit():
    cv2.place(x=66666, y=66666)
    cv_dibu.place(x=66666, y=66666)


def btn22():
    global filename2
    global str2
    global res2
    if filename2 == '':
        tk.messagebox.showinfo('提示', '请选择一个音频，若有疑问可以点击左下角帮助查看详细使用方法')
        return
    str2 = yuyin_str(filename2)

    input2.delete('1.0', 'end')
    input2.insert('end', str2)

    res2 = gettsres(str2)
    res2show.delete('1.0', 'end')
    res2show.insert('end', res2)


def btn2_clear():
    input2.delete('1.0', 'end')
    input2filename.delete('1.0', 'end')
    res2show.delete('1.0', 'end')


def jqb2():
    setText(res2)


def file2():
    global filename2
    filenames = tk_f.askopenfilenames(title='选择音频', filetypes=[(' 音频 ', '*.wav *.mp3'), ])
    if len(filenames) != 0:
        filename2 = filenames[0]
    else:
        filename2 = ''
    input2filename.delete('1.0', 'end')
    input2filename.insert('end', filename2)


##############################################4个翻译  3333333333


def btn3():
    cv3.place(x=-5, y=-5)
    cv1.place(x=66666, y=66666)
    cv2.place(x=66666, y=66666)
    cv4.place(x=66666, y=66666)
    cv_dibu.place(x=272, y=752)
    b_dibu1.config(relief='solid')
    b_dibu2.config(relief='solid')
    b_dibu4.config(relief='solid')
    b_dibu3.config(relief='flat')


def btn3_exit():
    cv3.place(x=66666, y=66666)
    cv_dibu.place(x=66666, y=66666)


def btn33():
    global filename3
    global str3
    global res3
    if filename3 == '':
        tk.messagebox.showinfo('提示', '请选择一个图片，若有疑问可以点击左下角帮助查看详细使用方法')
        return
    str3 = pic_str1(filename3)
    if str3 == '':
        tk.messagebox.showinfo('提示', '请选择一张带有可翻译文字的图片')
        return
    input3.delete('1.0', 'end')
    input3.insert('end', str3)

    res3 = gettsres(str3)

    res3show.delete('1.0', 'end')
    res3show.insert('end', res3)


def btn3_clear():
    input3.delete('1.0', 'end')
    input3filename.delete('1.0', 'end')
    res3show.delete('1.0', 'end')


def jqb3():
    setText(res3)


def file3():
    global filename3
    filenames = tk_f.askopenfilenames(title='选择图片', filetypes=[(' 图片 ', '*.jpg *.jpeg *.png *.bmp '), ])
    if len(filenames) != 0:
        filename3 = filenames[0]
    else:
        filename3 = ''
    input3filename.delete('1.0', 'end')
    input3filename.insert('end', filename3)


##############################################4个翻译  4444444444

def btn4():
    cv4.place(x=-5, y=-5)
    cv1.place(x=66666, y=66666)
    cv2.place(x=66666, y=66666)
    cv3.place(x=66666, y=66666)
    cv_dibu.place(x=272, y=752)
    b_dibu1.config(relief='solid')
    b_dibu2.config(relief='solid')
    b_dibu3.config(relief='solid')
    b_dibu4.config(relief='flat')


def btn4_exit():
    cv4.place(x=66666, y=66666)
    cv_dibu.place(x=66666, y=66666)


def btn44():
    global filename4
    global str4
    global res4
    if filename4 == '':
        tk.messagebox.showinfo('提示', '请选择一个图片，若有疑问可以点击左下角帮助查看详细使用方法')
        return
    str4 = pic_str2(filename4)

    input4.delete('1.0', 'end')
    input4.insert('end', str4)

    res4 = gettsres(str4)
    res4show.delete('1.0', 'end')
    res4show.insert('end', res4)


def btn4_clear():
    input4.delete('1.0', 'end')
    input4filename.delete('1.0', 'end')
    res4show.delete('1.0', 'end')


def jqb4():
    setText(res4)


def file4():
    global filename4
    filenames = tk_f.askopenfilenames(title='选择图片', filetypes=[(' 图片 ', '*.jpg *.jpeg *.png *.bmp '), ])
    if len(filenames) != 0:
        filename4 = filenames[0]
    else:
        filename4 = ''
    input4filename.delete('1.0', 'end')
    input4filename.insert('end', filename4)


##############################################四个调用#################################################

##############################################设置里的按钮

def btn_option():
    cvoption.place(x=-5, y=-5)
    b_option_exit.place(x=1110, y=0)
    b_login.place(x=66666, y=66666)
    cv.place(x=66666, y=66666)
    cvlogin.place(x=66666, y=66666)

    b_option.place(x=66666, y=66666)
    b_help.place(x=66666, y=66666)


def btn_option_exit():
    cv.place(x=-5, y=-5)
    b_login.place(x=0, y=0)
    b_option_exit.place(x=66666, y=66666)
    cvoption.place(x=66666, y=66666)
    b_option.place(x=1110, y=754)
    b_help.place(x=0, y=754)


def btn_option_logout():
    global islogin
    if islogin:
        islogin = False
        tk.messagebox.askyesno('确认退出', '确认退出账号吗？')
    else:
        tk.messagebox.showinfo('未登录', '未登录下无法退出')


def btn_option_distory():
    global islogin
    if islogin:
        tk.messagebox.askyesno('确认注销账号吗', '是否确认注销账号？(注销十五天内可以撤销该操作)')
    else:
        tk.messagebox.showinfo('未登录', '未登录下无法注销账号')


def skin_to_color(c1, c2, c3):
    global bgcolor
    global fgcolor
    global btbgcolor
    bgcolor = c1
    fgcolor = c2
    btbgcolor = c3
    cv.config(bg=bgcolor)
    cv1.config(bg=bgcolor)
    cv2.config(bg=bgcolor)
    cv3.config(bg=bgcolor)
    cv4.config(bg=bgcolor)
    cv_dibu.config(bg=bgcolor)
    cvhelp.config(bg=bgcolor)
    cvlogin.config(bg=bgcolor)
    cvfankui.config(bg=bgcolor)
    cvoption.config(bg=bgcolor)
    cv_dibu.config(bg=bgcolor)
    b_help.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_dibu1.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_dibu2.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_dibu3.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_dibu4.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b1.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b2.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b3.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b4.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b1_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b2_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b3_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b4_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt11.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt12.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt13.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt20.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt21.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt22.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt23.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt30.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt31.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt32.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt33.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt40.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt41.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt42.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    bt43.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_login.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b1_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b2_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b3_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b4_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_option.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_option_distory.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_option_changeusername.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_option_changepswd.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_option_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_login_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_login.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_fankui.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_fankui_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_option_logout.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_help_exit.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_login_login.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)
    b_login_signup.config(bg=btbgcolor, fg=fgcolor, activebackground=btbgcolor, activeforeground=fgcolor)

    input1.config(bg=bgcolor, fg=fgcolor, )
    input2.config(bg=bgcolor, fg=fgcolor, )
    input3.config(bg=bgcolor, fg=fgcolor, )
    input4.config(bg=bgcolor, fg=fgcolor, )
    input2filename.config(bg=bgcolor, fg=fgcolor, )
    input3filename.config(bg=bgcolor, fg=fgcolor, )
    input4filename.config(bg=bgcolor, fg=fgcolor, )
    res1show.config(bg=bgcolor, fg=fgcolor, )
    res2show.config(bg=bgcolor, fg=fgcolor, )
    res3show.config(bg=bgcolor, fg=fgcolor, )
    res4show.config(bg=bgcolor, fg=fgcolor, )
    login_username.config(bg=bgcolor, fg=fgcolor, )
    login_password.config(bg=bgcolor, fg=fgcolor, )

    l0.config(bg=bgcolor, fg=fgcolor)
    text10.config(bg=bgcolor, fg=fgcolor)
    text11.config(bg=bgcolor, fg=fgcolor)
    text12.config(bg=bgcolor, fg=fgcolor)
    text20.config(bg=bgcolor, fg=fgcolor)
    text21.config(bg=bgcolor, fg=fgcolor)
    text22.config(bg=bgcolor, fg=fgcolor)
    text23.config(bg=bgcolor, fg=fgcolor)
    text30.config(bg=bgcolor, fg=fgcolor)
    text31.config(bg=bgcolor, fg=fgcolor)
    text32.config(bg=bgcolor, fg=fgcolor)
    text33.config(bg=bgcolor, fg=fgcolor)
    text40.config(bg=bgcolor, fg=fgcolor)
    text41.config(bg=bgcolor, fg=fgcolor)
    text42.config(bg=bgcolor, fg=fgcolor)
    text43.config(bg=bgcolor, fg=fgcolor)
    login_l1.config(bg=bgcolor, fg=fgcolor)
    option_l1.config(bg=bgcolor, fg=fgcolor)
    login_l2.config(bg=bgcolor, fg=fgcolor)
    option_l2.config(bg=bgcolor, fg=fgcolor)
    fankui_l2.config(bg=bgcolor, fg=fgcolor)
    login_l3.config(bg=bgcolor, fg=fgcolor)
    login_l4.config(bg=bgcolor, fg=fgcolor)
    help_l00.config(bg=bgcolor, fg=fgcolor)
    help_l0.config(bg=bgcolor, fg=fgcolor)
    help_l1.config(bg=bgcolor, fg=fgcolor)
    help_l2.config(bg=bgcolor, fg=fgcolor)
    help_l3.config(bg=bgcolor, fg=fgcolor)
    help_l4.config(bg=bgcolor, fg=fgcolor)


def btn_option_skin_white():
    skin_to_color('#ffffff', 'black', '#ffffff')


def btn_option_skin_black():
    skin_to_color('#2b2b2b', 'white', '#191919')


def btn_option_skin_red():
    skin_to_color('#e37f7f', 'black', '#ee6262')


def btn_option_skin_yellow():
    skin_to_color('#fff885', 'black', '#fef22b')


def btn_option_skin_green():
    skin_to_color('#8bff85', 'black', '#66fe5f')


def btn_option_skin_blue():
    skin_to_color('#80f2ff', 'black', '#67e1ff')


def btn_option_skin_purple():
    skin_to_color('#ce95ff', 'black', '#c37efe')


##############################################反馈

def btn_fankui():
    global islogin
    if not islogin:
        tk.messagebox.showinfo('未登录', '未登录下无法提交反馈，请登陆后再进行操作')
        return
    cvoption.place(x=66666, y=66666)
    cvfankui.place(x=-5, y=-5)
    b_login.place(x=66666, y=66666)


def btn_fankui_exit():
    cvoption.place(x=-5, y=-5)
    cvfankui.place(x=66666, y=66666)
    b_login.place(x=0, y=0)


def fankui_new_qu(q, num, val, isdanxuan, wlen):
    cvnew = tk.Label(cvfankui, bg=bgcolor, relief='flat')
    fankuivar1 = tkinter.StringVar()
    fankuivar1.set(num)
    fankui_q_l1 = tk.Label(cvnew, font=('等线', 13), text=q, bg=bgcolor, width=wlen, height=1, relief='flat')
    fankui_q_l1.pack(side='left')
    for str in val:
        if isdanxuan:
            radio1 = tkinter.Radiobutton(cvnew, font=('等线', 13), variable=fankuivar1, value=str, text=str, bg=bgcolor,
                                         fg=fgcolor, activebackground=bgcolor, activeforeground=fgcolor)
            radio1.pack(side='left')
        else:
            fankui_ck1 = tk.Checkbutton(cvnew, font=('等线', 13), text=str, bg=bgcolor, fg=fgcolor,
                                        activebackground=bgcolor, activeforeground=fgcolor)
            fankui_ck1.pack(side='left')
    return cvnew


def btn_fankui_submit():
    tk.messagebox.showinfo('提交成功', '感谢反馈')
    cvoption.place(x=-5, y=-5)
    cvfankui.place(x=66666, y=66666)


##############################################登录里的按钮

def btn_login():
    cvlogin.place(x=-5, y=-5)
    cv.place(x=-5, y=-5)
    cvoption.place(x=66666, y=66666)

    b_login.place(x=66666, y=66666)
    b_option.place(x=66666, y=66666)
    b_help.place(x=66666, y=66666)

    b_login_exit.place(x=1110, y=0)


def btn_login_exit():
    cvlogin.place(x=66666, y=66666)
    b_option.place(x=1110, y=754)
    b_login.place(x=0, y=0)
    b_login_exit.place(x=66666, y=66666)
    b_help.place(x=0, y=754)


def btn_login_login():
    tk.messagebox.showinfo('登录成功', '登录成功')

    global islogin
    islogin = True
    b_login.place(x=66666, y=66666)
    btn_login_exit()


##############################################帮助界面


def btn_help():
    cvhelp.place(x=-5, y=-5)
    b_login.place(x=66666, y=66666)
    b_option.place(x=66666, y=66666)
    b_help.place(x=66666, y=66666)


def btn_help_exit():
    cvhelp.place(x=66666, y=66666)
    b_option.place(x=1110, y=754)
    b_login.place(x=0, y=0)
    b_help.place(x=0, y=754)


#####################################################################################################
if __name__ == '__main__':
    root = tk.Tk()
    root.title('多交互模式翻译')
    root.geometry('1200x800+400+100')
    root.configure(bg=bgcolor)

    ##############################################首页
    cv = tk.Canvas(root, bg=bgcolor, width=1220, height=900, relief='flat')
    cv.place(x=-5, y=-5)
    l0 = tk.Label(cv, font=('等线', 22), text='欢迎使用，请点击您想用的方式进行翻译输入', bg=bgcolor, width=38, height=2, )
    l0.place(x=333, y=70)
    b1 = tk.Button(cv, font=('等线', 15), text='文字翻译 ', bg=btbgcolor, fg=fgcolor, width=17, height=17, relief='solid',
                   command=btn1)
    b2 = tk.Button(cv, font=('等线', 15), text='音频识别翻译 ', bg=btbgcolor, fg=fgcolor, width=17, height=17, relief='solid',
                   command=btn2)
    b3 = tk.Button(cv, font=('等线', 15), text='图片上的文字翻译', bg=btbgcolor, fg=fgcolor, width=17, height=17, relief='solid',
                   command=btn3)
    b4 = tk.Button(cv, font=('等线', 15), text='图片上的文字翻译 ', bg=btbgcolor, fg=fgcolor, width=17, height=17, relief='solid',
                   command=btn4)
    b1.place(x=100, y=200)
    b2.place(x=370, y=200)
    b3.place(x=640, y=200)
    b4.place(x=910, y=200)

    ##############################################第1个翻译界面
    cv1 = tk.Canvas(root, bg=bgcolor, width=1220, height=900, )
    cv1.place(x=-2222, y=-11130)
    text10 = tk.Label(cv1, font=('等线', 22), text='文字输入翻译', bg=bgcolor, width=12, height=2, )
    text10.place(x=525, y=18)
    text11 = tk.Label(cv1, font=('等线', 19), text='待翻译文字:', bg=bgcolor, width=9, height=2, )
    text11.place(x=70, y=88)
    text12 = tk.Label(cv1, font=('等线', 19), text='翻译结果:', bg=bgcolor, width=9, height=2, )
    text12.place(x=610, y=88)

    b1_exit = tk.Button(cv1, font=('等线', 13), text='返回', bg=btbgcolor, fg=fgcolor, width=10, height=2, relief='solid',
                        command=btn1_exit)
    b1_exit.place(x=1110, y=0)

    bt11 = tk.Button(cv1, font=('等线', 13), text='获取翻译结果', bg=btbgcolor, fg=fgcolor, width=12, height=2, relief='solid',
                     command=btn11)
    bt11.place(x=465, y=151, )
    bt12 = tk.Button(cv1, font=('等线', 12), text='翻译结果复制到剪切板', bg=btbgcolor, fg=fgcolor, width=19, height=2,
                     relief='solid', command=jqb1)
    bt12.place(x=1010, y=151, )
    bt13 = tk.Button(cv1, font=('等线', 12), text='清空输入', bg=btbgcolor, fg=fgcolor, width=12, height=2, relief='solid',
                     command=btn1_clear)
    bt13.place(x=1010, y=516, )
    #           输入框
    varstr1 = tk.StringVar()
    input1 = tk.Entry(cv1, font=('等线', 22), bg='white', fg=fgcolor, show=None, width=22, textvariable=varstr1,
                      relief='solid')
    input1.place(x=74, y=151, width=333, height=122)
    #           结果显示
    res1show = tk.Text(cv1, font=('等线', 18), bg='white', fg=fgcolor, width=28, height=21, relief='solid')
    res1show.place(x=622, y=151, )

    ##############################################第2个翻译界面
    cv2 = tk.Canvas(root, bg=bgcolor, width=1220, height=900, )
    cv2.place(x=-2222, y=-11130)
    text20 = tk.Label(cv2, font=('等线', 22), text='音频识别翻译', bg=bgcolor, width=12, height=2, )
    text20.place(x=525, y=18)
    text21 = tk.Label(cv2, font=('等线', 19), text='待翻译音频:', bg=bgcolor, width=14, height=2, )
    text21.place(x=40, y=88)
    text22 = tk.Label(cv2, font=('等线', 19), text='翻译结果:', bg=bgcolor, width=9, height=2, )
    text22.place(x=610, y=88)
    text23 = tk.Label(cv2, font=('等线', 19), text='识别文字结果:', bg=bgcolor, width=14, height=2, )
    text23.place(x=50, y=223)

    b2_exit = tk.Button(cv2, font=('等线', 13), text='返回', bg=btbgcolor, fg=fgcolor, width=10, height=2, relief='solid',
                        command=btn2_exit)
    b2_exit.place(x=1110, y=0)

    bt20 = tk.Button(cv2, font=('等线', 13), text='选择音频', bg=btbgcolor, fg=fgcolor, width=11, height=1, relief='solid',
                     command=file2)
    bt20.place(x=310, y=104, )
    bt21 = tk.Button(cv2, font=('等线', 13), text='获取翻译结果', bg=btbgcolor, fg=fgcolor, width=14, height=2, relief='solid',
                     command=btn22)
    bt21.place(x=465, y=151, )
    bt22 = tk.Button(cv2, font=('等线', 12), text='翻译结果复制到剪切板', bg=btbgcolor, fg=fgcolor, width=19, height=2,
                     relief='solid',
                     command=jqb2)
    bt22.place(x=1010, y=151, )
    bt23 = tk.Button(cv2, font=('等线', 12), text='清空输入', bg=btbgcolor, fg=fgcolor, width=12, height=2, relief='solid',
                     command=btn2_clear)
    bt23.place(x=1010, y=516, )
    #           输入框
    input2filename = tk.Text(cv2, font=('等线', 18), bg='white', width=28, height=2, relief='solid')
    input2filename.place(x=74, y=151, )
    input2 = tk.Text(cv2, font=('等线', 18), bg='white', width=28, height=15, relief='solid')
    input2.place(x=74, y=296, )
    #           结果显示
    res2show = tk.Text(cv2, font=('等线', 18), bg='white', width=28, height=21, relief='solid')
    res2show.place(x=622, y=151, )

    ##############################################第3个翻译界面
    cv3 = tk.Canvas(root, bg=bgcolor, width=1220, height=900, )
    cv3.place(x=-2222, y=-11130)
    text30 = tk.Label(cv3, font=('等线', 22), text='图片文字翻译', bg=bgcolor, width=12, height=2, )
    text30.place(x=525, y=18)
    text31 = tk.Label(cv3, font=('等线', 19), text='待翻译图片:', bg=bgcolor, width=9, height=2, )
    text31.place(x=70, y=88)
    text32 = tk.Label(cv3, font=('等线', 19), text='翻译结果:', bg=bgcolor, width=9, height=2, )
    text32.place(x=610, y=88)
    text33 = tk.Label(cv3, font=('等线', 19), text='  文字结果:', bg=bgcolor, width=9, height=2, )
    text33.place(x=50, y=223)

    b3_exit = tk.Button(cv3, font=('等线', 13), text='返回', bg=btbgcolor, fg=fgcolor, width=10, height=2, relief='solid',
                        command=btn3_exit)
    b3_exit.place(x=1110, y=0)

    bt30 = tk.Button(cv3, font=('等线', 13), text='选择图片', bg=btbgcolor, fg=fgcolor, width=11, height=1, relief='solid',
                     command=file3)
    bt30.place(x=310, y=104, )
    bt31 = tk.Button(cv3, font=('等线', 13), text='获取翻译结果', bg=btbgcolor, fg=fgcolor, width=14, height=2, relief='solid',
                     command=btn33)
    bt31.place(x=465, y=151, )
    bt32 = tk.Button(cv3, font=('等线', 12), text='翻译结果复制到剪切板', bg=btbgcolor, fg=fgcolor, width=19, height=2,
                     relief='solid',
                     command=jqb3)
    bt32.place(x=1010, y=151, )
    bt33 = tk.Button(cv3, font=('等线', 12), text='清空输入', bg=btbgcolor, fg=fgcolor, width=12, height=2, relief='solid',
                     command=btn3_clear)
    bt33.place(x=1010, y=516, )
    #           输入框
    input3filename = tk.Text(cv3, font=('等线', 18), bg='white', width=28, height=2, relief='solid')
    input3filename.place(x=74, y=151, )
    input3 = tk.Text(cv3, font=('等线', 18), bg='white', width=28, height=15, relief='solid')
    input3.place(x=74, y=296, )
    #           结果显示
    res3show = tk.Text(cv3, font=('等线', 18), bg='white', width=28, height=21, relief='solid')
    res3show.place(x=622, y=151, )

    ##############################################第4个翻译界面
    cv4 = tk.Canvas(root, bg=bgcolor, width=1220, height=900, )
    cv4.place(x=-2222, y=-11130)
    text40 = tk.Label(cv4, font=('等线', 22), text='图片识物翻译', bg=bgcolor, width=12, height=2, )
    text40.place(x=525, y=18)
    text41 = tk.Label(cv4, font=('等线', 19), text='待识别并翻译图片:', bg=bgcolor, width=14, height=2, )
    text41.place(x=70, y=88)
    text42 = tk.Label(cv4, font=('等线', 19), text='翻译结果:', bg=bgcolor, width=9, height=2, )
    text42.place(x=610, y=88)
    text43 = tk.Label(cv4, font=('等线', 19), text='识别文字结果:', bg=bgcolor, width=14, height=2, )
    text43.place(x=50, y=223)

    b4_exit = tk.Button(cv4, font=('等线', 13), text='返回', bg=btbgcolor, fg=fgcolor, width=10, height=2, relief='solid',
                        command=btn4_exit)
    b4_exit.place(x=1110, y=0)

    bt40 = tk.Button(cv4, font=('等线', 13), text='选择图片', bg=btbgcolor, fg=fgcolor, width=11, height=1, relief='solid',
                     command=file4)
    bt40.place(x=310, y=104, )
    bt41 = tk.Button(cv4, font=('等线', 13), text='获取翻译结果', bg=btbgcolor, fg=fgcolor, width=14, height=2, relief='solid',
                     command=btn44)
    bt41.place(x=465, y=151, )
    bt42 = tk.Button(cv4, font=('等线', 12), text='翻译结果复制到剪切板', bg=btbgcolor, fg=fgcolor, width=19, height=2,
                     relief='solid',
                     command=jqb4)
    bt42.place(x=1010, y=151, )
    bt43 = tk.Button(cv4, font=('等线', 12), text='清空输入', bg=btbgcolor, fg=fgcolor, width=12, height=2, relief='solid',
                     command=btn4_clear)
    bt43.place(x=1010, y=516, )
    #           输入框
    input4filename = tk.Text(cv4, font=('等线', 18), bg='white', width=28, height=2, relief='solid')
    input4filename.place(x=74, y=151, )
    input4 = tk.Text(cv4, font=('等线', 18), bg='white', width=28, height=15, relief='solid')
    input4.place(x=74, y=296, )
    #           结果显示
    res4show = tk.Text(cv4, font=('等线', 18), bg='white', width=28, height=21, relief='solid')
    res4show.place(x=622, y=151, )

    ##############################################底部

    cv_dibu = tk.Canvas(root, bg=bgcolor, width=1220, height=125, relief='flat')
    cv_dibu.place(x=-2222, y=-11130)
    b_dibu1 = tk.Button(cv_dibu, font=('等线', 13), text='文字翻译 ', bg=btbgcolor, fg=fgcolor, width=17, height=2,
                        relief='solid', command=btn1)
    b_dibu2 = tk.Button(cv_dibu, font=('等线', 13), text='音频识别翻译 ', bg=btbgcolor, fg=fgcolor, width=17, height=2,
                        relief='solid', command=btn2)
    b_dibu3 = tk.Button(cv_dibu, font=('等线', 13), text='图片上的文字翻译 ', bg=btbgcolor, fg=fgcolor, width=17, height=2,
                        relief='solid', command=btn3)
    b_dibu4 = tk.Button(cv_dibu, font=('等线', 13), text='图片上的文字翻译 ', bg=btbgcolor, fg=fgcolor, width=17, height=2,
                        relief='solid', command=btn4)
    b_dibu1.pack(side='left')
    b_dibu2.pack(side='left')
    b_dibu3.pack(side='left')
    b_dibu4.pack(side='left')

    ##############################################登录
    cvlogin = tk.Canvas(root, bg=bgcolor, width=1220, height=900, )
    cvlogin.place(x=-2222, y=-11130)

    b_login_exit = tk.Button(cvlogin, font=('等线', 13), text='返回', bg=btbgcolor, fg=fgcolor, width=10, height=2,
                             relief='solid',
                             command=btn_login_exit)
    b_login_exit.place(x=1100, y=0)

    login_l1 = tk.Label(cvlogin, font=('等线', 17), text='用户名:', bg=bgcolor, width=12, height=2, )
    login_l1.place(x=422, y=132)
    login_l2 = tk.Label(cvlogin, font=('等线', 17), text='密码:', bg=bgcolor, width=12, height=2, )
    login_l2.place(x=422, y=233)
    login_username = tk.Entry(cvlogin, font=('等线', 17), show=None, relief='solid', )
    login_username.place(x=577, y=141)
    login_password = tk.Entry(cvlogin, font=('等线', 17), show='*', relief='solid', )
    login_password.place(x=577, y=247)
    login_l3 = tk.Label(cvlogin, font=('等线', 14), text='没有账号？ ', bg=bgcolor, width=12, height=2, )
    login_l3.place(x=565, y=531)
    login_l4 = tk.Label(cvlogin, font=('等线', 14), text='使用其他方式登录 ', bg=bgcolor, width=16, height=2, )
    login_l4.place(x=571, y=421)

    login_img = ImageTk.PhotoImage(Image.open('./.idea/bgg.png'))
    login_l5 = tk.Label(cvlogin, image=login_img)
    login_l5.place(x=572, y=451)
    b_login_login = tk.Button(cvlogin, font=('等线', 14), text='登录', bg=btbgcolor, fg=fgcolor, width=22, height=2,
                              relief='solid', command=btn_login_login)
    b_login_login.place(x=555, y=315)
    b_login_signup = tk.Button(cvlogin, font=('等线', 14), text='注册', bg=btbgcolor, fg=fgcolor, width=22, height=2,
                               relief='solid', )
    b_login_signup.place(x=555, y=575)

    ##############################################设置页面
    cvoption = tk.Canvas(root, bg=bgcolor, width=1220, height=900, )
    cvoption.place(x=-2222, y=-11130)
    b_option_exit = tk.Button(cvoption, font=('等线', 13), text='返回', bg=btbgcolor, fg=fgcolor, width=10, height=2,
                              relief='solid',
                              command=btn_option_exit)
    b_option_exit.place(x=1100, y=0)

    option_l1 = tk.Label(cvoption, font=('等线', 16), text='主题颜色选项', bg=bgcolor, width=12, height=2)
    option_l1.place(x=555, y=68)

    b_option_skin_to_white = tk.Button(cvoption, font=('等线', 16), text='白天', bg='white', fg='black',
                                       activebackground='white', activeforeground='black', width=9, height=4,
                                       relief='solid', command=btn_option_skin_white)
    b_option_skin_to_white.place(x=110, y=150)
    b_option_skin_to_black = tk.Button(cvoption, font=('等线', 16), text='黑夜', bg='#191919', fg='white',
                                       activebackground='#2b2b2b', activeforeground='white', width=9, height=4,
                                       relief='solid', command=btn_option_skin_black)
    b_option_skin_to_black.place(x=260, y=150)
    b_option_skin_to_red = tk.Button(cvoption, font=('等线', 16), text='红色', bg='#ee6262', fg='black',
                                     activebackground='#ee6262', width=9, height=4, relief='solid',
                                     command=btn_option_skin_red)
    b_option_skin_to_red.place(x=410, y=150)
    b_option_skin_to_yellow = tk.Button(cvoption, font=('等线', 16), text='黄色', bg='#fff885', fg='black',
                                        activebackground='#fff885', width=9, height=4, relief='solid',
                                        command=btn_option_skin_yellow)
    b_option_skin_to_yellow.place(x=560, y=150)
    b_option_skin_to_green = tk.Button(cvoption, font=('等线', 16), text='绿色', bg='#8bff85', fg='black',
                                       activebackground='#8bff85', width=9, height=4, relief='solid',
                                       command=btn_option_skin_green)
    b_option_skin_to_green.place(x=710, y=150)
    b_option_skin_to_green = tk.Button(cvoption, font=('等线', 16), text='蓝色', bg='#80f2ff', fg='black',
                                       activebackground='#80f2ff', width=9, height=4, relief='solid',
                                       command=btn_option_skin_blue)
    b_option_skin_to_green.place(x=860, y=150)
    b_option_skin_to_green = tk.Button(cvoption, font=('等线', 16), text='紫色', bg='#ce95ff', fg='black',
                                       activebackground='#ce95ff', width=9, height=4, relief='solid',
                                       command=btn_option_skin_purple)
    b_option_skin_to_green.place(x=1010, y=150)

    option_l2 = tk.Label(cvoption, font=('等线', 16), text='账号相关', bg=bgcolor, width=12, height=2, )
    option_l2.place(x=555, y=322)

    b_option_changeusername = tk.Button(cvoption, font=('等线', 16), text='更改用户名', bg=btbgcolor, fg=fgcolor, width=9,
                                        height=1, relief='solid', )
    b_option_changeusername.place(x=500, y=425)
    b_option_changepswd = tk.Button(cvoption, font=('等线', 16), text='更改密码', bg=btbgcolor, fg=fgcolor, width=9, height=1,
                                    relief='solid', )
    b_option_changepswd.place(x=650, y=425)
    b_option_logout = tk.Button(cvoption, font=('等线', 16), text='退出账号', bg=btbgcolor, fg=fgcolor, width=9, height=1,
                                relief='solid', command=btn_option_logout)
    b_option_logout.place(x=570, y=485)
    b_option_distory = tk.Button(cvoption, font=('等线', 16), text='注销账号', bg=btbgcolor, fg=fgcolor, width=9, height=1,
                                 relief='solid', command=btn_option_distory)
    b_option_distory.place(x=570, y=585)

    b_fankui = tk.Button(cvoption, font=('等线', 16), text='反馈', bg=btbgcolor, fg=fgcolor, width=22, height=2,
                         command=btn_fankui, relief='solid', )
    b_fankui.place(x=484, y=666)

    ##############################################反馈页面
    cvfankui = tk.Canvas(root, bg=bgcolor, width=1220, height=900, )
    cvfankui.place(x=-2222, y=-11130)
    fankui_l1 = tk.Label(cvfankui, font=('等线', 22), text='问卷与反馈', bg=bgcolor, width=22, height=2)
    fankui_l1.place(x=444, y=13)
    b_fankui_exit = tk.Button(cvfankui, font=('等线', 13), text='返回', bg=btbgcolor, fg=fgcolor, width=10, height=2,
                              relief='solid', command=btn_fankui_exit)
    b_fankui_exit.place(x=1110, y=0)

    fk_q1 = fankui_new_qu('您的性别', '1', ['男', '女', '不愿透露'], True, 7)
    fk_q2 = fankui_new_qu('您对电子产品每天使用频率', '2', ['每天1小时以下', '每天1-3小时', '3小时以上'], True, 22)
    fk_q3 = fankui_new_qu('您以前是否使用过相似的软件', '3', ['是', '否'], True, 24)
    fk_q4 = fankui_new_qu('您对该软件的使用频率', '4', ['不是每天都使用', '每天都使用但次数较少', '每天使用次数较多'], True, 19)
    fk_q5 = fankui_new_qu('您对该软件的总体满意度', '5', ['很不满意', '有些不满意', '一般', '比较满意', '非常满意'], True, 20)
    fk_q6 = fankui_new_qu('您认为该软件是否能满足您的功能需求', '6', ['很难满足', '有一些不满足', '基本都能满足'], True, 31)
    fk_q7 = fankui_new_qu('您对该软件的翻译功能满意度', '7', ['很不满意', '有些不满意', '一般', '比较满意', '非常满意'], True, 24)
    fk_q8 = fankui_new_qu('您对该软件的交互输入的满意度', '8', ['很不满意', '有些不满意', '一般', '比较满意', '非常满意'], True, 26)
    fk_q9 = fankui_new_qu('您对首页的满意度', '11', ['很不满意', '有些不满意', '一般', '比较满意', '非常满意'], True, 15)
    fk_q10 = fankui_new_qu('您对设置的满意度', '12', ['很不满意', '有些不满意', '一般', '比较满意', '非常满意'], True, 15)
    fk_q11 = fankui_new_qu('您对帮助的满意度', '13', ['很不满意', '有些不满意', '一般', '比较满意', '非常满意'], True, 15)
    fk_q12 = fankui_new_qu('您使用最多的功能', '9', ['文字输入翻译', '音频输入翻译', '图片文字翻译', ' 图片识物翻译'], True, 15)
    fk_q13 = fankui_new_qu('您使用最少的功能', '10', ['文字输入翻译', '音频输入翻译', '图片文字翻译', ' 图片识物翻译'], True, 15)
    fk_q14 = fankui_new_qu('您认为该软件做的好的部分', '14', ['文字输入翻译', '音频输入翻译', '图片文字翻译', ' 图片识物翻译', '设置系统', '帮助系统'], False, 22)

    x = 110
    y = 80
    for fk in [fk_q1, fk_q2, fk_q3, fk_q4, fk_q5, fk_q6, fk_q7, fk_q8, fk_q9, fk_q10, fk_q11, fk_q12, fk_q13, fk_q14]:
        fk.place(x=x, y=y)
        y += 30
    fankui_l2 = tk.Label(cvfankui, font=('等线', 13), text='您的建议或者任何想说的话：', bg=bgcolor, width=24, height=2)
    fankui_l2.place(x=x, y=y)
    fk_input = tk.Text(cvfankui, font=('等线', 13), bg='white', width=111, height=5, relief='solid')
    fk_input.place(x=x, y=y + 50)
    b_fankui_submit = tk.Button(cvfankui, font=('等线', 16), text='提交', bg=btbgcolor, fg=fgcolor, width=16, height=2,
                                relief='solid', command=btn_fankui_submit, )
    b_fankui_submit.place(x=484, y=711)

    ##############################################帮助页面
    cvhelp = tk.Canvas(root, bg=bgcolor, width=1220, height=900, )
    cvhelp.place(x=-2222, y=-11130)

    b_help_exit = tk.Button(cvhelp, font=('等线', 13), text='返回', bg=btbgcolor, fg=fgcolor, width=10, height=2,
                            relief='solid', command=btn_help_exit)
    b_help_exit.place(x=1110, y=0)

    help_l0 = tk.Label(cvhelp, font=('等线', 22), text='帮助', bg=bgcolor, width=12, height=2, )
    help_l0.place(x=535, y=22)
    help_l00 = tk.Label(cvhelp, font=('等线', 18), bg=bgcolor, width=86, height=5,
                        text='打开软件进入软件首页，可以在首页选择所需使用的功能进入使用。\n'
                             '右下角的设置与反馈进入后可以进行软件设置和反馈提交。左上角可 \n'
                             '以登录后进行反馈建议的提交、和对账号相关的操作。                      \n'
                             '进入翻译页面之后，从底部可以随时跳转到别的翻译功能页面，点击\n'
                             '右上角的返回可以随时返回到首页。                                                  ', )

    help_l00.place(x=52, y=82)
    help_l1 = tk.Label(cvhelp, font=('等线', 16), bg=bgcolor, width=86, height=5,
                       text='文字翻译\n'
                            '文字翻译可以在左侧的输入栏通过打字输入待翻译语句，点击中间获取翻译结果按钮，\n'
                            '翻译结果将会显示在右边的结果显示框里，中英文输入自动识别检测翻译。结果显示出\n'
                            '来后可以点击右侧上面的按钮将翻译结果一键复制到剪切版便于粘贴，也可以点击右侧\n'
                            '下面的按钮清空已输入文本和结果，重新输入待翻译文本。                                           ', )

    help_l1.place(x=112, y=212)
    help_l2 = tk.Label(cvhelp, font=('等线', 16), bg=bgcolor, width=86, height=6,
                       text='音频识别翻译\n'
                            '音频识别翻译可以在左侧点击选择音频来选择一段待翻译音频，(音频中的文字声音最好  \n'
                            '较为清晰)，选择音频后点击中间的获取翻译结果按钮，语音的原文将会显示在左侧显示  \n'
                            '框中，翻译结果将会显示在右边的结果显示框里，中英文输入自动识别检测翻译，结果显\n'
                            '示出来后可以点击右侧上面的按钮将翻译结果一键复制到剪切版便于粘贴，也可以点击右\n'
                            '侧下面的按钮清空已选择的文件和翻译结果，重新选择待输入文件。                               ', )
    help_l2.place(x=112, y=327)
    help_l3 = tk.Label(cvhelp, font=('等线', 16), bg=bgcolor, width=86, height=6,
                       text='图片文字识别翻译\n'
                            '图片文字识别翻译可以在左侧点击选择图片来选择一张待翻译的文字图片，(图片上需要有\n'
                            '可翻译文字)，选择图片后点击中间的获取翻译结果按钮，图片的原文将会显示在左侧显示\n'
                            '框中，翻译结果将会显示在右边的结果显示框里，中英文输入自动识别检测翻译，结果显  \n'
                            '示出来后可以点击右侧上面的按钮将翻译结果一键复制到剪切版便于粘贴，也可以点击右  \n'
                            '侧下面的按钮清空已选择的文件和翻译结果，重新选择待输入文件。                                    ', )
    help_l3.place(x=112, y=460)
    help_l4 = tk.Label(cvhelp, font=('等线', 16), bg=bgcolor, width=86, height=6,
                       text='图片物品识别翻译\n'
                            '图片文字识别翻译可以在左侧点击选择图片来选择一张待翻译的文字图片，(图片上需要有\n'
                            '可识别物品)，选择图片后点击中间的获取翻译结果按钮，图片上物品名称将会显示在左侧\n'
                            '框中，翻译结果将会显示在右边的结果显示框里，中英文输入自动识别检测翻译，结果显  \n'
                            '示出来后可以点击右侧上面的按钮将翻译结果一键复制到剪切版便于粘贴，也可以点击右  \n'
                            '侧下面的按钮清空已选择的文件和翻译结果，重新选择待输入文件。                                    ', )
    help_l4.place(x=112, y=595)

    ##############################################   首页上其他按钮

    b_login = tk.Button(root, font=('等线', 13), text='登录', bg=btbgcolor, fg=fgcolor, width=9, height=2, relief='solid',
                        command=btn_login, )
    b_login.place(x=0, y=0)
    b_option = tk.Button(root, font=('等线', 13), text='设置与反馈', bg=btbgcolor, fg=fgcolor, width=9, height=2,
                         relief='solid',
                         command=btn_option, )
    b_option.place(x=1110, y=754)
    b_help = tk.Button(root, font=('等线', 13), text='帮助', bg=btbgcolor, fg=fgcolor, width=9, height=2, relief='solid',
                       command=btn_help, )
    b_help.place(x=0, y=754)

    root.mainloop()
