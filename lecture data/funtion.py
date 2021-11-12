###################################################################
#funtion basics(알고 보면 우리가 배웠던 print, range, for 이런것들 다 누가 정의내리고 했던 함수이고 우리는 그걸 쓰고 있던 거임)

def open_account():#함수의 생성과 정의
    print("새로운 계좌가 생성되었습니다")

open_account()#함수의 호출

print("\n\n\n")

###################################################################
#passed value and return value
def depo(bal, mon):#정수형 변수의 전달값
    print(f"{bal+mon}")
    return bal+mon#정수형 반환값
bal=0
bal=depo(bal,200)
print(bal)

def depo(bal, mon):
    print(f"{bal+mon}")
    return bal,mon#이런 식으로 두 값을 동시에 반환 가능하다
bal, mon=depo(100,200)
print(bal, mon)

print("\n\n\n")

###################################################################
#setting default
def profile(name,age=17,main_lang="python"):#함수의 변수 선언 부분에 미리 값을 특정하면 함수 호출시 값을 따로 적지 않으면 그 값으로 초기화
    print(f"name : {name}\tage={age}\tmain lang : {main_lang}")

profile("iron")#age와 main_lang이 초기화된 값으로 출려되는 모습
profile("spider")

print("\n\n\n")

###################################################################
#keyword value
def profile(name,age=17,main_lang="python"):
    print(f"{name} {age} {main_lang}")

profile(name="iron",main_lang="python",age=21)#키워드에 해당하는 값을 넣어도 정상적으로 출력
profile(age=25,name="thor",main_lang="c++")

print("\n\n\n")

###################################################################
#variable factor
def profile(name,age,*lang):#*lang이란 가변 인자로 넣고 싶은 변수대로 넣어도 됨(전달값이 가변할때 사용 용이)
    print(f"{name} {age}",end=" ")
    for lang in lang:
        print(lang,end=" ")
    print()

profile("iron",21,"java")
profile("thor",22,"html","c#","c++","c")

print("\n\n\n")

###################################################################
#local variable and global variable
gun=10#이게 전역변수
def checkpoint(sold):
    gun=20#checkpoint 함수 내에서만 활성화되는 지역변수
    gun-=sold
    print(gun)
checkpoint(2)
print(gun)#위 값과 이 값이 다르다

def checkpoint(sold):
    global gun#전역변수의 선언
    #global gu2=20#이런 식으로는 선언이 불가능
    gun-=sold
    print(gun)