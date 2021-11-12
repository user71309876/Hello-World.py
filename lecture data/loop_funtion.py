###########################################################################################
#if
weather="sunny"
if weather=="sunny":
    print("take a umbrella")#string으로도 사용할 수 있다
    
tem=20
if 10<tem<30:
    print("very hot")#굳이 and를 안붙여도 된다

print("\n\n\n")

###########################################################################################
#for

app=range(0,20,2)#range(A,B,C) A부터 시작해 B 미만으로 끝나고, C만큼 증가 혹은 감소한다
print(list(app))#2씩 증가한 모습

for i in range(1,6):#0,1,2,3,4
    print(f"대기번호 : {i}")

star=["iron","thor","tree"]
for i in star:#sizeof(star)만큼 반복함
    print(i)#증가하는 변수인 i는 star[i]를 반환함

scores={"수학":0,"영어":50,"코딩":100}
for sub,sco in scores.items():#scores에 있는 key와 value를 sub와 soc에 반환함
    print(sub,sco)

print("\n\n\n")

###########################################################################################
#while
cus="thor"
index=5
while index>=1:#while문의 형식
    print(f"{cus}, coffe is ready. {index} left")
    index-=1
    if index==0:
        print("coffe is in trash can")

print("\n\n\n")

###########################################################################################
#contiune and break
absent=[2,5]
no_book=[7]
for stu in range(1,11):
    if stu in absent:#stu in absent가 맞으면 true, 틀리면 false
        continue#만약 if 문이 실행됬다면 continue를 실행 즉, 그때 stu에 대한 반복문을 무시하고 다음 반복문 실행
    elif stu in no_book:
        print(f"{stu}! follow me. you dead day. class is over")
        break#반복문을 끝냄
    print(f"{stu}read a book")

print("\n\n\n")

###########################################################################################
#one line "for" funtion
stu=[1,2,3,4,5]
print(stu)
stu=[i+100 for i in stu]#stu 배열의 각 값에 100을 더함
print(stu)

stu=["iron","spider","thors"]
stu=[len(i) for i in stu]#배열 안의 string의 길이를 넣음
print(stu)

stu=["iron","spider","thors"]
stu=[i.upper() for i in stu]#배열 안의 string을 대문자로 변환
print(stu)

#여기서 i.upper()은 변환될 값을 반환
#for i in stu는 반복할 갯수를 반환