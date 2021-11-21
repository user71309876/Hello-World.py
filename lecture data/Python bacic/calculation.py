#숫자처리함수
print(abs(-5)) #(-5)에 대한 절대값
print(pow(4,2))#4^2의 값
print(max(5,12))#두개의 값 중에 큰 값을 반환
print(min(5,12))#두개의 값 중에 작은 값을 반환
print(round(3.14),2)#값을 반올림하되 소수점 2재짜리까지 표시

from math import *#using everything funtion in math library
print(floor(4.99))#내림
print(ceil(3.14))#올림
print(sqrt(16))#제곱근

#랜덤함수
from random import *
print(random())#0.0 ~ 1.0 사이의 임의값 반환
print(random()*10)#0.0~10.0 사이의 임의값 반환
print(int(random()*10))#0 ~ 10 미만의 int형 임의값 반환
print(int(random()*10)+1)#1 ~ 11 미만의 int형 임의값 반환

print(randrange(1,46))#1 ~ 46 미만의 int형 임의값 반환
print(randint(1,45))#1 ~ 45 이하의 int형 임의값 반환

arr=[1,2,3,4,5]
shuffle(arr)#arr list의 순서를 섞음
print(arr)

print(sample(arr,1))#arr list 값 중 1개만 뽑음