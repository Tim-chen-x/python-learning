#常见数据类型--->type()获取指定的字面量或变量的类型
# print("Hello")
# print(type("Hello"))
#
# print(type(10))
# print(type(3.14))
# print(type(True))
# print(type(False))
# print(type(None))
#
# num = 100
# print(type(num))
# #
# # #常见数据类型---->isinstance(数据，类型)-->bool值-->判定数据是否是指定的类型，是：True,否：False
# #
# print(isinstance(num,int))
# print(isinstance(num,float))

#字符串
#定义字符串的三种方式
# s1 = "Hello World"#双引号定义
# s2 = 'Python'#单引号定义
# s3 = """
#     欢迎大家进入这里
#     大家随便逛逛~~~
# """#三引号定义（多行字符串）
#
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
#
#
# #转义字符 \' \" \n \t
msg = 'It\' very good!'
print(msg)
#
# msg2 = "It's very good"
# print(msg2)
#
# msg3 = "Hello的意思是\"你好\""
# print(msg3)
#
# print("\t欢迎大家进入这里\n\t\t大家随便逛逛~~~")#\n 换行 \t 缩进
#


#字符串的拼接
# s1 = "人生苦短""我用Python"",OK"
# print(s1)
#
# msg1 = "人生苦短"
# msg2 = "我用Python"
#
# print("龟叔说："+msg1 + "," + msg2)
#
# #案例:--->str(int)--->将int类型的数字转为字符串
# name = "陈培翔"
# age = 20
# pro = "电气工程"
# hobby = "Python"
# print("大家好,我叫" + name + ",今年" + str(age) + "岁,学习的专业是" + pro + ",爱好"  +  hobby)



#字符串格式化--> %s 占位符
# name = "陈培翔"
# age = 20
# pro = "电气工程"
# hobby = "Python"
# print("大家好，我叫%s,今年%s岁,专业是%s,爱好是%s"% (name, age, pro, hobby))
#
# #字符串格式化-->第二种方式：f"..{变量名/表达式}.."---->推荐方式
# s1 = "人生苦短"
# s2 = "我用Python"
# print(f"龟叔说：{s1},{s2}")



