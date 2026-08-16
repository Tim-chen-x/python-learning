# import math
#
#
# def add(a,b):
#     return a+b
# c = add(1,2)
# print(c)
#
# def circle_area(radius):
#     """
#     this function is used to calculate the area of a circle
#     :param radius: 圆的半径
#     :return: 圆的面积
#     """
#     return round(math.pi * radius * radius , 4)
#
# help(circle_area)
# print(circle_area(5))
#
# def rectangle(width,height):
#     """
#     this function is used to calculate the area and the lengths of a rectangle
#     :param width: 长
#     :param height: 宽
#     :return: 面积，周长
#     """
#     return width*height , 2*(width + height)
# a,b = rectangle(3,4)
# print(a,b)
#
# def put_line():
#     print("---------------------")
#     return rectangle(1,2)
# print(put_line())

#嵌套函数  栈的结构:后入先出


#----------------------------------案例--------------------------------------
# 案例1
# def rating(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     else:
#         return "D"
#
# score = int(input("请输入你的分数:"))
# print(rating(score))

#案例2
# def huiwen(st):
#     st1 = st[::-1] #字符串反转要用st[::-1]
#     if st1 == st:
#         return True
#     else:
#         return False
# st = input("请输入字符串:")
# print(huiwen(st))

#案例3
# def conversion(second):
#     return round(second/60,2),round(second/3600,2)
# second = int(input("请输入秒:"))
# minute,hour = conversion(second)
# print(hour,minute)

#案例4
def triangle_judge(a,b,c):
    if a==b and b==c:
        print("该三角形是等边三角形")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("该三边无法组成三角形")
    elif a==b or b==c or c==a:
        print("该三角形是等腰三角形")
    else:
        print("该三角形是普通三角形")

a = int(input())
b = int(input())
c = int(input())
triangle_judge(a,b,c)