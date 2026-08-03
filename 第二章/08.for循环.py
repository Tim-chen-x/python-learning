# msg = input("请输入需要遍历的字符串：")
#
# for s in msg:
#     print(f"元素:{s}")
# else :
#     print("循环结束")



#print(*) 自带换行效果，每一次输出都会另起一行
#print("*",end="")end表示的是每一次输出以什么结束;默认 \n,表示换行
#1.接受键盘录入
m = int(input("请输入长方形的长度:"))
n = int(input("请输入长方形的宽度:"))

#2.打印长方形
for j in range(n):
    for i in range(m):
        print("*",end="  ")
    print()
