from tkinter import *

root=Tk()
root.title("Nado GUI")#프로그램 이름 정하기
root.geometry("640x480")

txt=Text(root,width=30,height=5)#텍스트창을 넣기
txt.pack()

txt.insert(END,"input")#미리 텍스트 넣기

e=Entry(root,width=30)#Text와 다른 점은 엔터를 못친다는 점
e.pack()
e.insert(0,"input one line")

def btncmd():
    #내용 출력
    print(txt.get("1.0",END))#1 : 첫번째 라인, 0 : 0번째 column 위치(column은 문장이라 보면 됨)
    print(e.get())#애는 그냥 get 쓰면 됨
    
    #내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)

btn1=Button(root,text="click",command=btncmd)
btn1.pack()

root.mainloop()