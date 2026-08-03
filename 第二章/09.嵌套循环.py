

#关键字
# break:只能够出现在循环中，表示结束、跳出循环的含义（break跳出循环时，while后面的else中的代码将不会执行
# continue:只能够出现在循环中，表示中断本次循环，直接进入下一轮循环



while True:
    user = input("请输入正确的账号：")
    password = input("请输入正确的密码：")

    if user == "" or password == "":
        print("账号密码不能为空，请重新输入")
        continue
    if user == "admin" and password == "666888":
        print("恭喜登录成功，进入B站首页")
        break
    elif user == "zhangsan" and password == "123456":
        print("恭喜登录成功，进入B站首页")
        break
    elif user == "taoge" and password == "888666":
        print("恭喜登录成功，进入B站首页")
        break
    else:
        print("用户名或密码错误，请重新输入")