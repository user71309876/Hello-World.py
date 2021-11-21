from random import *
arr=range(1,21)
arr=list(arr)
print("--당첨자 발표--\n치킨 당첨자 :",sample(arr,1))
arr.remove(1)
print("커피 당첨자 :",sample(arr,3),"\n--축하합니다--")