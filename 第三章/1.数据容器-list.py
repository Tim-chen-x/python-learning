#列表操作
#定义
s = [56,90,88,65,90,"A","Hello",True]
print(type(s))

#获取列表元素
#获取
print(s[0])#正向索引，从0开始
print(s[-8])#反向索引，从-1开始

print(s[2])
print(s[-6])

#修改
s[5] = "ABC"
#s[10] = "DEF"#如果指定的索引超出范围，将会报错list assignment index out of range

print(s)

#删除
del s[6]
print(s)

#遍历
for item in s:
    print(item)



#--------------------------------列表list切片-------------------------------
#定义列表
s = ["A","C","H","K","L","B","D","X","C","U"]


# 切片操作 s[开始索引:结束索引:步长]
print(s[0:5:1])
print(type(s[0:5:1]))

print(s[:5:1])

print(s[:5:])

print(s[:5])

print(s[0:5:2])

print(s[0:-9:1])


#----------------------------------列表list常用方法-------------------------------------
#列表定义
s = [56,90,88,65,90,100,209,72,145]
print(s)

# append():在列表的尾部追加元素
s.append(188)
print(s)

#insert():在指定索引之前，插入元素
s.insert(3,80)
print(s)

#remove():移除列表中第一个匹配到的元素
s.remove(90)
print(s)

#pop():删除列表中指定索引位置的元素并返回（如果未指定索引，默认删除最后一个元素）
e = s.pop(1)
print(s)
print(e)

s.pop()
print(s)

#sort():排序
s.sort()
print(s)

#reverse():反转列表元素
s.reverse()
print(s)




#--------------------------列表list案例------------------------------------------
#案例一:将用户输入的10个数字，存储到一个列表里，并将列表里的数字进行排序，输出最大值最小值和平均值

# s = []          # 初始化一个空列表
# num = 0
# for i in range(0,10):
#     s.append(int(input("请输入数字:")))   # 使用 append() 追加元素
#
# # for j in range(0,10):
# #     num = num + s[j]
#
# #  sum():求和函数
#
# s.sort()    #默认从小到大排序
# print(s)
# print(f"最大值为:{s[-1]}")
# print(f"最小值为:{s[0]}")
# print(f"平均值为:{sum(s)/len(s)}")







# #案例二:合并两个列表中的元素，并对合并的结果进行去重处理（去掉列表中重复的元素）
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
#
# #1.合并列表
# # for i in range(len(num_list2)):
# #     num_list1.append(num_list2[i])
# #
# # print(num_list1)   #有点麻烦的做法
# for num in num_list1:
#     num_list2.append(num)
#
# print("合并后的原始列表:",num_list2)
#
# #2.去除重复元素
# new_list = []
# for num in num_list2:
#     if num not in new_list:  #in:判断元素是否存在于列表中，如果存在，则返回True;不存在，返回False
#         new_list.append(num)
#
#
# print("去除重复记录后的列表:",new_list)

#案例二(简化版):合并两个列表中的元素，并对合并的结果进行去重处理（去掉列表中重复的元素）
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]

#1.合并列表
# 解包:将列表这一类容器解开成一个一个独立的元素
# 组包:讲多个值合并到一个容器

num_list = [*num_list1,*num_list2]
# 法三:num_list = num_list1 + num_list2

print("合并后的原始列表:",num_list)

#2.去除重复元素
new_list = []
for num in num_list:
    if num not in new_list:  #in:判断元素是否存在于列表中，如果存在，则返回True;不存在，返回False
        new_list.append(num)


print("去除重复记录后的列表:",new_list)






#案例三:  生成1-20的平方列表 -->range(1,21) 包含开始，不包含结束
#方式一:传统方法
num_list = []
for i in range(1,21):
    num_list.append(i**2)

print(num_list)

#方式二:列表推导式 ---->就是按照一定的规则快速生成一个列表的方法 -->语法格式:[要插入的值 for i in 序列/列表]
num_list2 = [i**2 for i in range(1,21)]
print(num_list2)

#案例四:从一个数字列表中提取所有的偶数，并计算其平方，组成一个新的列表
num_list3 = [12,32,45,77,80,92,33,57,97,98]
new_list = [i**2 for i in num_list3 if i%2==0]  #列表推导式，这也太方便了
print(new_list)

