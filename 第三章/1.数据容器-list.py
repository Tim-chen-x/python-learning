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