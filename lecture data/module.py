###################################################################
#module

import module_definition#module_definition을 정의함, 모듈이나 페키지만 가능
module_definition.price(3)
module_definition.price_morning(4)
module_definition.price_soldier(5)

import module_definition as md#module_definition을 md로 정의함
md.price(3)
md.price_morning(4)
md.price_soldier(5)

from module_definition import price_morning#module_definition에서 price_morning만 불러오겟다

#price(3)#이러면 여기서 에러 납니다
price_morning(4)
#price_soldier(5)#여기도요

from module_definition import *#module_definition에 있는 모든 class, funtion등을 불러오겠다

price(3)
price_morning(4)
price_soldier(5)#다 실행되는 모습

from module_definition import price_soldier as price2#이렇게도 사용 가능합니다

price2(3)#잘 되는 모습

print("\n\n\n")