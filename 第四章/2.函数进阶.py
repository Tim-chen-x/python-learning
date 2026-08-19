#---------------------------------变量作用域---------------------
# import math
#
# num = 100
# def circle_area(radius):
#     area = math.pi * (radius ** 2)
#     global num
#     num = 10
#     print(num)
#     return area
# print(circle_area(10))
# print(num)

#------------------------------函数参数传递方式----------------------------------
# def total_scores(chinese,math,english):
#     return chinese +math +english
# a = 100
# b = 100
# c = 90
# print(total_scores(90,math = 10,english = 10))
# print(total_scores(a,b,c))

#默认参数:  def total_scores(chinese,math,english = 100):

#------------------------------不定长参数传递-------------------------------------
# def scores(*args):
#     return max(args), min(args), sum(args)/len(args)
# print(scores(a,b,c))

# def scores(*args,**kwargs):
#     avg = sum(args) / len(args)
#     if kwargs.get("round") is not None:
#         avg =round(avg,kwargs['round'])
#     return max(args), min(args) ,avg
# print(scores(10,16,17,round=2))
# print(scores(10,16,17,round=3))


#----------------------------函数的参数类型-----------------------------------------
# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
#
# def calc(x,y,oper):
#     return oper(x,y)
#
# print(calc(1,2,subtract))

#----------------------------匿名函数----------------------------------
#定义方式
#lambda 参数列表 : 函数体

# def out_line():
#     print("-----------")
#
# out_line()
#
# out_line1 = lambda : print("---------------------")
#
# out_line1()
#
# add = lambda x, y: x + y
# print(add(1, 2))
#
# #案例
# data_list = ["C++","C","PHP","Rust","Python","Java","JavaScript"]
#
# data_list.sort(key = lambda item:len(item), reverse = True)
# print(data_list)

#案例
#案例1：计算n的阶乘
#递归调用（先层层递进，再逐层回归）:指的是在函数中自己调用自己的情况 -------------> 一定要有终结点

"""
jc(10) = 10 * jc(9)
jc(9) = 9 * jc(8)
jc(8) = 8 * jc(7)
jc(7) = 7 * c(6)
jc(6) = 6 * jc(5)
jc(5) = 5 * jc(4)
jc(4) = 4 * jc(3) = 4 * 6 = 24
jc(3) = 3 * jc(2) = 3 * 2 = 6
jc(2) = 2 * jc(1) = 2 * 1 = 2
jc(1) = 1
"""
def jc(n):
    if(n==1):
        return 1
    else:
        return n*jc(n-1)


print(jc(10))


