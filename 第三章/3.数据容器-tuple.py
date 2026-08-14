#列表有什么特点？
#元素可重复、有序、可以修改

#元组一旦定义完成，不可修改
#元组 介绍：元组是不可变的序列，类似于列表，但创建后不可修改
#     特点：可以存储不同类型的元素
#          元素可以重复、有序、不可以修改（支持索引访问、切片）




# #定义
# t1 = (80,95,78,50,76,80,85,20)
# print(t1)
# print(type(t1))
#
# # 索引访问
# print(t1[0])
# print(t1[-1])
#
# # 切片
# print(t1[0:5:2])
#
# # count() 统计元素的个数
# print(t1.count(80))
# # index() 获取元素的索引(第一个元素的位置)
# print(t1.index(80))
#
#
# # 注意点: 如果定义单元素的元组，单个元素之后要加上逗号
# t2 = ()
# print(type(t2))
# print(t2)
#
# t3 = (100,)
# print(t3)
# print(type(t3))



#--------------------------------元组tuple组包和解包----------------------------------------
# # 组包操作
# t1 = (5,7,9,10,2,23,12)
# t2 = 5,7,9,10,2,23,12
#
# print(t1)
# print(t2)
#
# # 解包操作
# # 基础解包（变量数量=容器的元素个数）
# a,b,c,d,e,f,g=t1
# print(a,b,c,d,e,f,g)
#
# # 扩展解包（* 收集剩余的所有元素，封装列表List）
# first,second,*other,last = t1
# print(first,second,other,last)
#
# *other,last2,last1 = t1
# print(other,last2,last1)




# #案例1:现有两个变量，分别为a = 10, b = 20,现需要将这两个变量值交换
# a = 10
# b = 20
#
# # #组包
# # t = b,a
# # #解包
# # a,b = t
#
# a,b=b,a
#
# print(a,b)
#
# #案例2
# a = 100
# b = 200
# c = 300
#
# #组包与解包操作
# c,a,b = a,b,c
#
# print(a,b,c)

#-------------------------------------------案例---------------------------------------------
#数据只是查看，不修改，所以用元组而不用列表
#方式一
# students = (("S001","王林",85,92,78),("S002","李慕婉",92,88,95),("S003","十三",78,85,82))
#
# print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3

#方式二:元组解包
students = (("S001","王林",85,92,78),("S002","李慕",92,88,95),("S003","十三",78,85,82))

print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3

    print(f"{id}\t{name}\t\t{chinese}\t\t{math}\t\t{english}\t\t{total}\t\t{avg:.3f}")  #保留小数位数


# Chinese_list = []
# for s in students:
#     Chinese_list.append(s[2])
# print(Chinese_list)
# Chinese_list.sort()
# print(f"语文最低分{Chinese_list[0]},最高分{Chinese_list[2]}")

#列表推导式
Chinese_list = [s[2] for s in students]
print(Chinese_list)
print(f"语文最低分{min(Chinese_list)},最高分{max(Chinese_list)}")