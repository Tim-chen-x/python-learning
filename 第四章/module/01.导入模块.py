# 1.导入模块  ----->调用方式:模块名.功能名
# import random
#
#
# for i in range(100):
#     print(random.randint(1,100))

# import random as r
# for i in range(100):
#     print(r.randint(1,100))


# 2.导入模块中的功能  from ... import ...
# from random import randint as rnd
#
# for i in range(100):
#     print(rnd(1,100))

# 3.导入模块中的所有功能
from random import *
for i in range(100):
    print(randint(1,100))