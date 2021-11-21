###################################################################
#print
print("python","java",sep=",")# sep 다음에 들어다는 string은 , 부분에 어느것을 넣을지 결정
print("cheer up dk",end="!")#문장의 끝부분에 들어갈 string을 결정
print("winner is dk")

import sys#python에서 기본 제공하는 함수를 제어하는거 같음
print("fuck",file=sys.stdout)#이건 나도 모르겠네....
print("python",file=sys.stderr)

scores={"수학":0,"영어":50,"코딩":100}
for sub,sco in scores.items():
    print(sub.ljust(8), str(sco).rjust(4),sep=":")#ljust(8)는 8칸 왼쪽정렬, rjust(4)는 4칸 오른쪽정렬
                                                  #단, string type만 됨
for num in range(1,11):
    print("waiting number",str(num).zfill(3))#3개의 공간을 확보하고 나머지 공간은 0으로 채운다

# ans=input("input any word : ")#항상 string으로 값을 반환
# print(ans)

print("\n\n\n")

###################################################################
#various output format
print("{0: >10}".format(500))#10공간을 두고 오른쪽 정렬을 하되 비어있는 공간은 공백으로 하라
print("{0: <10}".format(500))#10공간을 두고 왼쪽 정렬을 하되 비어있는 공간은 공백으로 하라
str=500
print(f"{str: >10}")#이렇게도 할 수 있음

str=500
print(f"{str: >+10}")#양수일때는 +, 음수일때는 -로 표시
str=-500
print(f"{str: >+10}")

str=500
print(f"{str:_<10}")#10공간을 두고 왼쪽 정렬을 하되 비어있는 공간은 _으로 하라

print("{0:+,}".format(1000000000000000000))#3자리마다 콤마를 붙어주고 부호까지 붙이기

print("{0:.2f}".format(5/3))#소수점 3번째 자리에서 반올림

print("{0:^<+30,.2f}".format(1000000000000))
#소수점 3번째 자리에서 반올림을 하고(.2f), 3자리마다 ','를 붙이고(,), 30자리를 확보하고(30),
# 부호를 붙이고(+),왼쪽 정렬을 하고(<),빈 공간에는 '^'을 넣는다
#순서 알고 있어야 함

print("\n\n\n")

###################################################################
#input/output file
sco_file=open("score.txt","w",encoding="utf8")
#score.txt라는 파일을 쓰기 용도로 열고(덮어쓰기로 됨) utf8로 한글을 칠 수 있게 만듬
print("math : 0",file=sco_file)#sco_file에 math : 0을 넣음, 줄바꿈이 자동으로 됨
print("eng : 50",file=sco_file)#이하동문
sco_file.close()#sco_file을 닫음

sco_file=open("score.txt","a",encoding="utf8")#이미 있던 텍스트에 이어쓰기 가능
sco_file.write("sci : 80\n")#이것슨 줄바꿈이 자동으로 안됨
sco_file.write("coding : 100")
sco_file.close()

sco_file=open("score.txt","r",encoding="utf8")#읽기 전용으로 파일을 열음
print(sco_file.read())
sco_file.close()

sco_file=open("score.txt","r",encoding="utf8")
print(sco_file.readline())#줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
print(sco_file.readline())
print(sco_file.readline())
print(sco_file.readline())
sco_file.close()

sco_file=open("score.txt","r",encoding="utf8")
while True:#무한반복
    line=sco_file.readline()
    if not line:#line에 아무것도 없으면 실행
        break
    print(line)
sco_file.close()

sco_file=open("score.txt","r",encoding="utf8")
line=sco_file.readlines()#list 형태로 저장
for line in line:
    print(line,end="")
sco_file.close()

print("\n\n\n")

###################################################################
#pickle(리스크나 클래스같은 자료형은 일반 입출력으로 저장 불가능. 그래서 pickle을 이용)
import pickle 
pro_file=open("profile.pickle","wb")#쓰기 목적과 바이너리 파일 정의, 피클에선 인코딩 해줄 필요 없음 
                                    #피클은 바이너리 써야 함
pro={ "name":"iron","age":"30","hobby":["soccer","golf",":badminton"]}
print(pro)
pickle.dump(pro,pro_file)#por에 있는 파일을 pro_file에 저장
pro_file.close()

pro_file=open("profile.pickle","rb")
pro2=pickle.load(pro_file)#pro_file에 있는 정보를 pro2에 저장
print(pro2)
pro_file.close()

print("\n\n\n")

###################################################################
#with
with open ("profile.pickle","rb") as profile_file:
#profile.pickle을 열고 그 값을 profile_file 변수에 저장
    print(pickle.load(profile_file))
#close() 이런거 안해줘도 됨

with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("Study python very hard")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())