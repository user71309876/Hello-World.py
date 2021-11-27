#값을 다중선택 가능
from tkinter import *

root=Tk()
root.title("Nado GUI")#프로그램 이름 정하기
root.geometry("640x480")

chkvar=IntVar()#chkvar에 int 형으로 값을 저장한다
chkbox=Checkbutton(root,text="do not see today",variable=chkvar)
# chkbox.select()#자동 선택 처리
# chkbox.deselect()#자동 선택 해제 처리
chkbox.pack()

chkvar2=IntVar()
chkbox2=Checkbutton(root,text="do not see week",variable=chkvar2)
#IntVar는 서로 따로 지정해주어야 함
chkbox2.pack()


def btncmd():
    print(chkvar.get())# 0 :체크 해제, 1 : 체크
    print(chkvar2.get())
    
    

btn1=Button(root,text="click",command=btncmd)
btn1.pack()

root.mainloop()