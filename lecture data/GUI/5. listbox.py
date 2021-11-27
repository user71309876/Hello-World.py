#여러가지 값들을 위젯으로 관리하는 함수, 회원가입할때 생년월일 고르는 박스라 생각하면 됨
from tkinter import *

root=Tk()
root.title("Nado GUI")#프로그램 이름 정하기
root.geometry("640x480")

listbox=Listbox(root,selectmode="extended",height=0)
"""
selectmode
1. extended : 여러개의 값을 고를 수 있음
2. single   : 하나의 값만 고를 수 있음

height
1. 0 : 모든 값을 보여줌
2. i : i가지 값만 보여줌
"""
listbox.insert(0,"apple")#0번째 인덱스에 apple를 넣겠다
listbox.insert(1,"strawbarry")
listbox.insert(2,"banana")
listbox.insert(END,"watermellon")#맨 마지막 인덱스에 watermellon을 넣겠다
listbox.insert(END,"grape")
listbox.pack()


def btncmd():
    # #삭제
    # listbox.delete(END)#맨 뒤의 항목을 삭제
    # listbox.delete(0)#맨 앞의 항목을 삭제

    # #갯수 확인
    # print("in list",listbox.size())
    
    # #항목 확인
    # print("item 1 to 3 : ",listbox.get(0,2))

    #선택된 항목 확인(위치로 반환)
    print("choosed item : ",listbox.curselection())
    
    

btn1=Button(root,text="click",command=btncmd)
btn1.pack()

root.mainloop()