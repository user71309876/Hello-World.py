###########################################################################################
#list(대괄호에 저장)
arr=[10,20,30]
print(arr)
arr=["rull","power","car"]
print(arr)
print(arr.index("rull"))#string의 index와 같음

arr.append("space")#list의 맨 뒷줄에 space string을 넣음 단, print문 내부에 넣으면 안됨
print(arr)
arr.insert(1,"drive")#list의 1번째 값에 "~"을 넣음 단, print문 내부에 넣으면 안됨
print(arr)
print(arr.pop())#list의 맨 뒷번에 있는 값을 빼서 그 값을 반환(뺀 list를 출력하는 것이 아님!)
print(arr)

print(arr.count("drive"))#string의 count와 같음

num_arr=[5,2,3,1,4]
num_arr.sort()#list를 12345처럼 정렬
print(num_arr)
num_arr.reverse()#list의 배열 순서를 바꿈
print(num_arr)
num_arr.clear()#list를 모두 지움
print(num_arr)

arr=["drive",11,True]#다양한 자료형과 함께 사용 가능
print(arr)
num_arr=[5,2,3,1,4]
num_arr.extend(arr)#num_arr의 뒤쪽에 arr list를 합침
print(num_arr)

num1=[1,2,3]
num2=4
print(num2 in num1)#num1 안에 num2의 유무를 true과 false로 반환

arr2=range(1,21)#1부터 21 미만의 숫자를 생성하고 배열로 생성. 단, 타입이 range로 됨

print("\n\n\n")

###########################################################################################
#dictionary
cabinet={3:"cave",100:"live"}#3번에 cave. 100번에 live를 선정
print(cabinet[3])#3번 키에 대한 값을 반환
print(cabinet.get(3))#3번 키에 대한 값을 반환
#print(cabinet[5])#5번 키가 없으면 에러
print(cabinet.get(5))#5번 키가 없으면 None을 반환
print(cabinet.get(5,"available"))#5번 키가 없으면 "available"을 반환

print(3 in cabinet)#3이라는 키의 유무를 true와 false로 반환

cabinet={"A-3":"cave","B-100":"live"}#A-3에 cave. B-100에 live를 선정
print(cabinet["A-3"])

print(cabinet)
cabinet["C-20"]="liver"#c-20의 키에 liver를 할당. 만약 c-20키가 있으면 liver로 바꿈

del cabinet["A-3"]#A-3에 대한 키와 값을 제거

print(cabinet.keys())#cabinet의 키를 반환
print(cabinet.values())#cabinet의 값을 반환
print(cabinet.items())#키와 값 모두 반환

cabinet.clear#cabinet 제거

print("\n\n\n")

###########################################################################################
#tuple(내용 변경이나 추가가 안됨. but 속도가 빠름)
menu=("beef","water")#tuple은 소괄호에 저장
print(menu[0])
print(menu[1])

(name,age,hobby)=("steve",20,"coding")#tuple형태로 변수에 값을 저장

print("\n\n\n")

###########################################################################################
#set(집합, 중복안됨, 순서 없음, 중괄호에 저장)
myset={1,2,3,3,3}
print(myset)#중복이 안되므로 {1,2,3}이렇게 나옴

java={"find","die","live"}
python=set(["find","chicken"])#list와 같이 []으로 정의를 하고 set()에 넣어도 됨

print(java&python)#java와 python의 교집합 반환
print(java.intersection(python))#java와 python의 교집합 반환

print(java | python)#java와 python의 합집합 반환. 순서 보장안됨
print(java.union(python))#java와 python의 합집합 반환. 순서 보장안됨

print(java-python)#java에python의 차집합
print(java.difference(python))#java에python의 차집합

python.add("milk")#python에서 milk를 추가
print(python)

java.remove("find")#java에서 find를 제거
print(java)

print("\n\n\n")

###########################################################################################
#changing data structure
menu={"coffe","milk","juice"}
print(menu,type(menu))#menu를 반환하고, menu의 자료형 타입을 반환

menu=list(menu)#자료형을 list로 변환
print(menu,type(menu))

menu=tuple(menu)#자료형을 tuple로 변환
print(menu,type(menu))