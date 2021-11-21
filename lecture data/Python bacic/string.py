# basic
sentence="나는 소년입니다"
print(sentence)#sentence 문자열을 출력
sentence="""나는 소녀입니다"""#""" (여기에 문자열을 넣을 수 있다) """

print("\n\n\n")

###########################################################################################
#slicing(배열의 처음은 0임)
junin="991205-1234567"
print(junin[7])#7째 있는 문자를 출력 ex)1
print(junin[0:2])#0번째부터 2번째 미만까지 출력
print(junin[:2])#처음부터 2번째 미만까지 출력
print(junin[7:])#7번째부터 끝까지 출력
print(junin[-7:])#뒤에서부터 7번째부터 끝까지 출력

print("\n\n\n")

###########################################################################################
#string processing funtion
python="Pytion is Amazing"
print(python.lower())#모든 문자가 소문자로 출력
print(python.upper())#모든 문자가 대문자로 출력
print(python[0].isupper())#0번째 문자가 대문자이냐?
print(len(python))#python의 길이를 출력
print(python.replace("python","java"))#phtyon이라는 문자열에서 python을 찾아서 java로 바꿈
print(python.index("n"))#python에서 n이 있는 위치를 출력
print(python.index("n",6))#pyton에서 6번째를 포함한 위치부터 n이 있는 위치를 출력

#print(python.index("java"))#python에서 java라는 문자가 없을 경우에는 index는 에러를 냄
print(python.find("java"))#python에서 java라는 문자가 없을 경우에는 find는 -1를 반환

print(python.count("n"))#python에서 n 문자가 몇번 나왔는지 출력

print("\n\n\n")

###########################################################################################
#string format
print("나는 %d살입니다"%20)#%d에 20을 출력
print("%c"%"A")#%c에 "A"라는 문자를 넣음
#%s에는 정수, 문자열, 문자 다 넣어도 됨
print("%s"%"파이썬")#%s에 "파이썬"이라는 문자열을 넣음
print("%s"%1)#%s에 1이라는 정수을 넣음
print("%s"%"A")#%s에 "A"이라는 문자을 넣음

print("%s %s"%("파란","빨간"))#%(~,~,~,~,~,~)순서대로 %s에 들어감
print("{}".format(20))#format()안에 있는 값이 {}에 들어감
print("{} {}".format("파란","빨간"))#format()안에 있는 값이 {}에 순서대로 들어감
print("{1} {0}".format("파란","빨간"))#format()안에 있는 값이 {}에 있는 값 순서대로 들어감

print("{age} {color}".format(age=20,color="빨간색"))#format안에 있는 age, color 값이 {}에 있는 age, format에 들어감

age=20
color="빨간"
print(f"{age} {color}")#앞에 f를 넣으면 {}안에 있는 변수대로 출력

print("\n\n\n")

###########################################################################################
#escape char
print("죽기좋은\n날씨네")#\n은 줄바꿈
print("\"죽기좋은\" 날씨네")#\", \'는 print문 안에서 문자로 취급
print("C:\\Users")#print문 내에서 (\\) 는 (\)로 출력
print("죽기좋은 날씨네\r살기좋은")#\r는 커서를 맨 앞으로 이동 그리고 \r 뒤에 있는 문자열을 출력
print("죽기좋좋\b은날씨네")#\b은 backspace를 한다
print("죽기좋은\t날씨네")#\t은 tab을 한다

