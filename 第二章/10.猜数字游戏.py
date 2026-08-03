# import random
# random_num = random.randint(1,100)
#
#
#
# while True:
#     num = int(input("请输入一个数字："))
#     if num>random_num:
#         print("你输入的数字大了")
#     elif num<random_num:
#         print("你输入的数字小了")
#     else:
#         print("你猜对了")
#         break


#作业1
# total = 0
# for i in range(1,1000):
#     if i % 5 ==0:
#        total += i
#
# print(total)

#作业2
num1=0
num2=0
msg="akiwksdfjwerongfirngiurewngvirenvgirwenfiugwjofijaiugnfiueafhgowaehnfgiuwerni"
for i in msg:
    if i == 'a':
        num1+=1
    if i == 'k':
        num2+=1
print(num1,num2)