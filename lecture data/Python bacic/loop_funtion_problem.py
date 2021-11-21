from random import *#random 라이브러리로 모든(import *)함수를 가져온다
total_cus=0#총 탑승한 승객 명수
for cus in range(1,51):#cus를 1부터 51 미만까지 반복
    time=randrange(5,51)#time에 5부터 51 미만의 랜덤만 정수형 값을 넣어줌
    if(4<time<16):#time 변수가 4 초과 16 미만일때
        print("[0]",end=" ")
        total_cus+=1
    else:#time 변수가 그 외일때
        print("[ ]",end=" ")
    print(f"{cus}번째 손님 (소요시간 : {time}분)")
print(f"\n총 탑승 승객 : {total_cus}분")