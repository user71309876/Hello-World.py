#값을 한가지만 선택 가능
from tkinter import *

root=Tk()
root.title("Nado GUI")#프로그램 이름 정하기
root.geometry("640x480")

Label(root,text="select menu").pack()#이렇게 써도 된다

burger_var=IntVar()#여기에 int 형으로 값을 저장
btn_burger1=Radiobutton(root, text="hanburger",value=1,variable=burger_var)
btn_burger1.select()
btn_burger2=Radiobutton(root, text="chese hanburger",value=2,variable=burger_var)
btn_burger3=Radiobutton(root, text="chicken hanburger",value=3,variable=burger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root,text="select drink").pack()

drink_var=StringVar()#여기에 string 형으로 값을 저장
btn_drink1=Radiobutton(root, text="coke",value="coke",variable=drink_var)
btn_drink1.select()
btn_drink2=Radiobutton(root, text="saida",value="saida",variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())#라이오버튼의 value를 반환한다
    print(drink_var.get())
    
btn1=Button(root,text="order",command=btncmd)
btn1.pack()

root.mainloop()