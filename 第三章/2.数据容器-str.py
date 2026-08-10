# 字符串的基本操作  ----->不可变的（无法修改）
# 字符串的特点：不可变性、有序性、可迭代行性

# s = "Hello-python"
# print(s[4])  #正向索引
# print(s[-8]) #反向索引
#
# # s[4] = "X"   错误！！！
# # print(s[4])
#
# for i in s:
#     print(i)    #遍历
#
# #  切片
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[6:12:1])
# print(s[6::1])
# print("----------------------------")
# print(s[-1:-7:-1])  #开始序列和结束序列的顺序必须和步长的方向一致


#-------------------------------------字符串常用方法---------------------------------------
s = "      Hello-Python-Hello-World       "


# find() 查找指定字符串 第一次 出现的索引位置
index = s.find("-")
print(index)

# count() 统计 子字符串 在指定字符串中出现的 次数
c = s.count("o")
print(c)

#upper() 转为大写
su = s.upper()
print(su)

#lower() 转为小写
sl = s.lower()
print(sl)

#split() 将字符串按指定字符串切割 为 list列表
slist = s.split("-")
print(slist)

#strip() 去除字符串两端的空格
ss = s.strip()
print(ss)

#replace() 将字符串中的指定子串替换为新内容
sr = s.replace("-","_")
print(sr)

#startswith/endswith 判断字符串是否以指定字符串开始/结束，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))

print("-----------------------------")
print(s)

# ------------------------------------字符串案例---------------------------------------
#案例一:邮箱格式验证:用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.）

# #1.接受用户输入邮箱
# mail = input("请输入邮箱：")
#
# #2. 判断邮箱格式
# if mail.count("@") == 1 and mail.count(".") >=1:
#     print(f"{mail}是合法邮箱")
# else:
#     print(f"{mail}是非法邮箱")

#方法二: in 运算符 ---->判断子串是否在字符串中，存在，返回True;否则，返回False
# #1.接受用户输入邮箱
# mail = input("请输入邮箱：")
#
# #2. 判断邮箱格式
# if mail.count("@") == 1 and "." in mail :
#     print(f"{mail}是合法邮箱")
# else:
#     print(f"{mail}是非法邮箱")


#-------------------------练习----------------------------------------
# #1.判断字符串是否是回文
# s = input("请输入字符串:")
# s1 = s[-1::-1]
# print(s1)
# if s1 == s :
#     print(f"{s}是回文字符串")
# else:
#     print(f"{s}不是回文字符串")

#2.将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来

slist = []                      # 初始化空列表，用于存储处理后的字符串

for i in range(1, 11):          # 循环10次，接收10个字符串
    s = input(f"请输入第{i}个字符串:")
    s1 = s[-1::-1]              # 反转字符串
    s2 = s1.upper()             # 转换为大写
    slist.append(s2)            # 追加到列表中


print(slist)

print("---------------------------")
print("处理后的列表内容:")
for item in slist:              # 遍历列表并输出
    print(item)
