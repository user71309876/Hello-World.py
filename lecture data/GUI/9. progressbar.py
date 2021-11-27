#진행상태를 표시하는 BAR
import time
import tkinter.ttk as ttk
from tkinter import *

root=Tk()
root.title("Nado GUI")#프로그램 이름 정하기
root.geometry("640x480")

progressbar=ttk.Progressbar(root,maximum=100,mode="indeterminate")
#mode
#indeterminate(확정되지 않은) : 프로그래스 바가 왕복 이동한다
#determinate(확정된) : 프로그래스 바가 왼쪽에서 오른쪽으로 계속 이동한다
progressbar.start(10)#10ms마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop()#작동 중지

btn1=Button(root,text="stop",command=btncmd)
btn1.pack()

p_var2=DoubleVar()
pgb2=ttk.Progressbar(root,maximum=100,length=150,variable=p_var2)
pgb2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01)#0.01초 대기
        p_var2.set(i)#pgb 값 설정
        pgb2.update()#ui 업데이트
        print(p_var2.get())
    
btn1=Button(root,text="start",command=btncmd2)
btn1.pack()

root.mainloop()