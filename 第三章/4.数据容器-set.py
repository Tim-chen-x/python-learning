# 集合set  ---->无序,不可重复,可修改
# # 定义
# s1 = {5,3,2,5}
# print(s1)
# print(type(s1))
#
# #定义空集合
# s2 = set()
# print(s2)
# print(type(s2))

#常见操作
s1 = {23,45,78,12,34}
print(s1)

#add()
s1.add(99)
print(s1)

# remove()
s1.remove(78)
print(s1)

# pop()
e = s1.pop()
print(e)
print(s1)

# clear()
s1.clear()
print(s1)

s2 = {"A","B","C","E"}
s3 = {"E","F","G","A","B"}

#difference() :求两个集合的差集（存在于第一个集合，不存在于第二个集合）
print(s2.difference(s3))
print(s3.difference(s2))

#intersection() :求两个集合的交集
print(s2.intersection(s3))

#union() :求两个集合的并集
print(s2.union(s3))



print(s2.symmetric_difference(s3))



