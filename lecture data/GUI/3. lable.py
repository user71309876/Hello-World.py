#label은 실제 동작하지 않고 이미지 혹은 텍스트만 보여줌
from tkinter import *

root=Tk()
root.title("Nado GUI")#프로그램 이름 정하기
root.geometry("640x480")

label1=Label(root,text="안녕하세요")
label1.pack()

green=PhotoImage(file="C:/Users/꼴뽁딱찌/Desktop/Python WorkStation/lecture data/GUI/images/green.png")



label2=Label(root,image=green)
label2.pack()

def change():
    label1.config(text="see you again")#label1의 text를 

    global red
    red=PhotoImage(file="C:/Users/꼴뽁딱찌/Desktop/Python WorkStation/lecture data/GUI/images/red.png")
    """
    그냥 red만 있을때는 빨간게 안나오는데 그 이유는 red가 지역변수여서 
    barbage collection(불필요한 메모리 공간 해제)이라는게 red를 지워서 그럼
    그래서 red를 전역변수로 설정해야 됨
    """
    label2.config(image=red)

btn1=Button(root,text="click",command=change)
btn1.pack()

root.mainloop()