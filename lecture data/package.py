# import package_definition.thailand
# trip_to=package_definition.thailand.ThailandPackage()
# trip_to.detail()

# from package_definition import *#package_definition안에 있는 모든 것을 사용하겠다
# trip_to=vietnam.VietnamePackage()#모든걸 사용하겠다고 했는데도 에러가 나는 모습
# trip_to.detail()#어떻게 된일 일까 
#package의 공개 범위를 설정해야 한다 그러기 위해선 __init__으로 설정 가능

from package_definition import *
trip_to=vietnam.VietnamPackage()
trip_to.detail()#잘 되는 모습

trip2=thailand.ThailandPackage()
trip2.detail()#thailand까지 설정했더니 잘 되는 모습

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
