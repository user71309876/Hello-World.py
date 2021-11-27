import tkinter.messagebox as msg
from tkinter import *

root=Tk()
root.title("Nado GUI")#프로그램 이름 정하기
root.geometry("640x480")

#기차 예메 시스템이라 가정
def info():
    msg.showinfo("Notice","Purchase has been successfully completed.")
    #"(메세지 타이틀)","(메세지 설명)"
def warn():
    msg.showwarning("Warning","This seat is already sold out.")
    #info와 메세지 아이콘 모양이 달라짐
def error():
    msg.showerror("Error","A payment error has occurrred.")
    #메세지 아이콘이 달라지고 소리가 남
def okcancel():
    msg.askokcancel("Ok / Cancel","This seat is for infants. Would you like to purchace?")
def retrycancel():
    response=msg.askretrycancel("Retry / Cancel","Temorary Error. Do you want to retry")
    if response==1:#retry
        print("retry")
    elif response==0:#cancel
        print("cancel")
    
def yesno():
    msg.askyesno("Yes / No","This seat is reverse. Would you like to purchace?")
def yesnocancel():
    response=msg.askyesnocancel(title=None,message="Purchace history was not save.\nDo you exit program after saving?")
    #yes = save and eixt
    #no = not save and exit
    #cancel = cancel program exit(continue working on the current screen)
    #앞에 "="을 붙임으로써 반응값을 가져올 수 있음
    print(response)#True,false,none -> yes 1, no 0, the rest
    if response==1:#yes
        print("yes")
    elif response==0:#no
        print("no")
    else:
        print("cancel")

Button(root,command=info,text="Notice").pack()
Button(root,command=warn,text="Warning").pack()
Button(root,command=error,text="Error").pack()
Button(root,command=okcancel,text="Ok / Cancel").pack()
Button(root,command=retrycancel,text="retrycancel").pack()
Button(root,command=yesno,text="Yes / No").pack()
Button(root,command=yesnocancel,text="Yes / No / Cancel").pack()

root.mainloop()