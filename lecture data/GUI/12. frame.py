import tkinter.messagebox as msg
from tkinter import *

root=Tk()
root.title("Nado GUI")#프로그램 이름 정하기
root.geometry("640x480")

Label(root,text="select menu").pack(side="top")
"""
<side>
"top"=위쪽으로 넣는다
"botton"=아래
"left"=왼쪽
"right"=오른쪽
"""

Button(root,text="ordering").pack(side="bottom")

frame_burger=Frame(root,relief="solid",bd=1)
frame_burger.pack(side="left",fill="both",expand="true")

Button(frame_burger,text="hamburger").pack()
Button(frame_burger,text="chese hamburger").pack()
Button(frame_burger,text="chicken hamburger").pack()

frame_drink=LabelFrame(root,text="drink")
frame_drink.pack(side="right",fill="both",expand="true")
Button(frame_drink,text="coke").pack()
Button(frame_drink,text="soda").pack()

root.mainloop()