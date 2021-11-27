import tkinter.ttk as ttk
from tkinter import *

root=Tk()
root.title("Nado GUI")#프로그램 이름 정하기
root.geometry("640x480")

values=[str(i)+"일" for i in range(1,32)]
combobox=ttk.Combobox(root,height=5,values=values)
#리스트에 있는 값들이 전달, values는 보여지는 목록 갯수
combobox.pack()
combobox.set("card payment date")#최초 목록 제목 설정

readonly_combobox=ttk.Combobox(root,height=10,values=values,state="readonly")#리스트에 있는 값들이 전달
readonly_combobox.current(0)#0번째 인덱스 값 기본값으로 설정
readonly_combobox.pack()

def btncmd():
    print(combobox.get())#선택된 값 표시
    print(readonly_combobox.get())#선택된 값 표시

btn1=Button(root,text="chose",command=btncmd)
btn1.pack()

root.mainloop()