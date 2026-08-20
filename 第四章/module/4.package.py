#1.import 包名.模块名    调用方法: 包名.模块名.功能名
# import utils.my_fun
# utils.my_fun.log_separator2()

#2.from 包名 import 模块名  调用方法:模块名.功能名
# from utils import my_raw
# print(my_raw.NAME)

#3.from 包名 import *  调用方法:模块名.功能名     (使用这种方法时，必须在__init__.py文件中加入__all__ = ["功能名",...]
# from utils import *
# print(my_raw.NAME)
# my_fun.log_separator2()

#4.from 包名.模块名 import 功能名   调用方法:功能名
# from utils.my_fun import log_separator2,log_separator3
# log_separator2()
# log_separator3()

#5.from 包名.模块名 import *   调用方法:功能名
# from utils.my_fun import *
# log_separator2()
# log_separator3()


#---------------------------路径问题----------------------------------
# 相对路径:从当前文件所在目录开始查找
# from utils import *
# print(my_raw.NAME)
# my_fun.log_separator2()

# 绝对路径:从项目的根目录下开始查找
from 第四章.utils import *
print(my_raw.NAME)
my_fun.log_separator2()


#总结:1.包就是一个文件夹，里面有很多python文件，每个文件就是一个模块
#    2.__init__.py文件作用:标识这是个包，而不是普通的文件夹;  指出在import * 时导入的模块列表（__all__=[]）
#    3.导入包的方式?