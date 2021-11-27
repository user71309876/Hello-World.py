from tkinter import *

root=Tk()
root.title("Nado GUI")#프로그램 이름 정하기

btn1=Button(root,text="버튼1")#Button(어느 창에 넣을 것인지,버튼 안에 넣을 글자는 무엇인지)
btn1.pack()#설정한 btn1을 넣는다

btn2=Button(root,padx=5,pady=10,text="버튼 2")#default버튼 크기값에 x와 y에 +=를 해준다
btn2.pack()                                   #default버튼 크기 값은 글자 양에 따라 달라진다

btn3=Button(root,padx=10,pady=5,text="버튼 3")
btn3.pack()

btn4=Button(root,width=10,height=5,text="버튼 4")#이건 아에 버튼 크기를 지정한다
btn4.pack()                                      #버튼 크기는 글자 양에 따라 달라지지 않는다

btn5=Button(root,fg="red",bg="yellow",text="버튼 5")#fg는 글자색, bg는 버튼 배경색
btn5.pack()

photo=PhotoImage(file="C:/Users/꼴뽁딱찌/Desktop/Python WorkStation/lecture data/GUI/images/green.png")
#동영상대로 해보니깐 안되서 주소를 저렇게 넣었습니다
btn6=Button(root,image=photo)
btn6.pack()

def btncmd():
    print("working")
btn7=Button(root,text="동작하는 버튼",command=btncmd)
btn7.pack()

root.mainloop()