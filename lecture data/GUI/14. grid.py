from tkinter import *

root=Tk()
root.title("Nado GUI")#프로그램 이름 정하기
root.geometry("640x480")

# btn1=Button(root,text="button 1")
# btn2=Button(root,text="button 2")

# btn1.grid(row=0,column=0)#위치를 정해서 그 자리에 넣는 느낌
# btn2.grid(row=1,column=1)

#맨 윗줄
btn_f16=Button(root,text="F16",width=5,height=2)
#절대적인 크기로 버튼 크기를 바꾼다
btn_f17=Button(root,text="F17",width=5,height=2)
btn_f18=Button(root,text="F18",width=5,height=2)
btn_f19=Button(root,text="F19",width=5,height=2)

btn_f16.grid(row=0,column=0,sticky=N+E+W+S,padx=3,pady=3)
#sticky : 동(E)서(W)남(S)북(N)으로 최대 크기까지 커저라!
#padx, pady : 각각 버튼 사이에 공간을 3으로 해라
btn_f17.grid(row=0,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_f18.grid(row=0,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_f19.grid(row=0,column=3,sticky=N+E+W+S,padx=3,pady=3)

#clear 줄
btn_clear=Button(root,text="clear",width=5,height=2)
btn_eueal=Button(root,text="=",width=5,height=2)
btn_div=Button(root,text="/",width=5,height=2)
btn_mul=Button(root,text="*",width=5,height=2)

btn_clear.grid(row=1,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_eueal.grid(row=1,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_div.grid(row=1,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_mul.grid(row=1,column=3,sticky=N+E+W+S,padx=3,pady=3)

#7시작줄
btn_7=Button(root,text="7",width=5,height=2)
btn_8=Button(root,text="8",width=5,height=2)
btn_9=Button(root,text="9",width=5,height=2)
btn_sub=Button(root,text="-",width=5,height=2)

btn_7.grid(row=2,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_8.grid(row=2,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_9.grid(row=2,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_sub.grid(row=2,column=3,sticky=N+E+W+S,padx=3,pady=3)

#4시작줄
btn_4=Button(root,text="4",width=5,height=2)
btn_5=Button(root,text="5",width=5,height=2)
btn_6=Button(root,text="6",width=5,height=2)
btn_add=Button(root,text="+",width=5,height=2)

btn_4.grid(row=3,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_5.grid(row=3,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_6.grid(row=3,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_add.grid(row=3,column=3,sticky=N+E+W+S,padx=3,pady=3)

#1시작줄 
btn_1=Button(root,text="1",width=5,height=2)
btn_2=Button(root,text="2",width=5,height=2)
btn_3=Button(root,text="3",width=5,height=2)
btn_enter=Button(root,text="enter",width=5,height=2)#세로로 합처짐

btn_1.grid(row=4,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_2.grid(row=4,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_3.grid(row=4,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_enter.grid(row=4,column=3,rowspan=2,sticky=N+E+W+S,padx=3,pady=3)#rowspan은 현재 위치로부터 아래쪽으로 몇줄을 더함

#0시작줄
btn_0=Button(root,text="0",width=5,height=2)
btn_point=Button(root,text=".",width=5,height=2)

btn_0.grid(row=5,column=0,columnspan=2,sticky=N+E+W+S,padx=3,pady=3)
btn_point.grid(row=5,column=2,sticky=N+E+W+S,padx=3,pady=3)








root.mainloop()