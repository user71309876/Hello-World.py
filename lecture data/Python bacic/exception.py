###################################################################
#error handling
try:#밑의 문장을 해보고 에러가 났을 때
    print("divisoin-only calculator")
    num1=int(input("input number"))
    num2=int(input("input number"))
    print(f"{num1} / {num2} = {int(num1/num2)}")
    
except ValueError:#이 에러가 맞으면 실행시켜라
    print("errer! you input wrong value")
    
except ZeroDivisionError as err:#이 에러가 맞으면 실행시키고 에러가 먼지도 출력해라
    print(err)
    
except Exception as err:#위 문장 중 해당하는 에러가 없으면 실행시켜라
    print("An unkown error has occurred")
    print(err)
    
print("\n\n\n")
    
###################################################################
#intentional error
try:
    print("divisoin-only calculator")
    num1=int(input("input number"))
    num2=int(input("input number"))
    if num1>=10 or num2>=10:#두 수 모드 10보다 크면
        raise ValueError#valueerror를 발생시켜라
    
    print(f"{num1} / {num2} = {int(num1/num2)}")
    
except ValueError:#이 에러가 맞으면 실행시켜라
    print("errer! you input wrong value")
    
print("\n\n\n")
    
###################################################################
#custom error handling
class BigNumberError(Exception):#Exception를 상속받는다, Exception도 하나의 클래스였던거임!
    def __init__(self, msg):
        self.msg=msg
    
    def __str__(self):
        return self.msg#입력받은 msg를 반환

try:
    print("divisoin-only calculator")
    num1=int(input("input number"))
    num2=int(input("input number"))
    if num1>=10 or num2>=10:
        raise BigNumberError(f"input value : {num1} , {num2}")
     
    print(f"{num1} / {num2} = {int(num1/num2)}")
    
except ValueError:
    print("errer! you input wrong value")
except BigNumberError as err:#반환한 값을 err에 저장
    print("error has occurred! Please input single digit")
    print(err)#그리고 출력
    
print("\n\n\n")
    
###################################################################
#finally(정상적으로 출력이 되든 에러가 발생하든 무조건 실행되는 구문)

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg=msg
    
    def __str__(self):
        return self.msg

try:
    print("divisoin-only calculator")
    num1=int(input("input number"))
    num2=int(input("input number"))
    if num1>=10 or num2>=10:
        raise BigNumberError(f"input value : {num1} , {num2}")
     
    print(f"{num1} / {num2} = {int(num1/num2)}")
    
except ValueError:
    print("errer! you input wrong value")
except BigNumberError as err:
    print("error has occurred! Please input single digit")
    print(err)
finally:#애는 마지막에 무조건 실행된다
    print("Thank you for using calculator")