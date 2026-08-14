#字典 --key不能重复(如果重复，后面的值会覆盖前面的值)、key必须是不可变类型（str,int,float,tuple）
#    --value可以是任意类型
#    --字典没有索引下标,不能根据索引获取值,只可以根据key获取value

#定义字典
# dict1 = {"王林":670,"李慕婉":608,"徐立国":688}
# print(dict1)
# print(type(dict1))
#
# #key不能是list,set,dict
# dict2 = {0:670,(1,2):608,'a':688}
# print(dict2)
#
# #访问
# print(dict1["王林"]) #获取
# dict1["王林"] = 700
# print(dict1)

#--------------------------------------常用操作--------------------------------------

# 添加/修改
# dict1["涛哥"] = 500
# print(dict1)
#
# # 删除
# score = dict1.pop("涛哥")
# print(score)
# del dict1["王林"]
#
# # 查询
# print(dict1["徐立国"])
# print(dict1.get("徐立国"))
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
#
#
# #遍历
# for k in dict1.keys():
#     print(f"{k}: {dict1[k]}")
#
#
# for s in dict1.items():
#     print(f"{s[0]}: {s[1]}")
#
# for k,v in dict1.items():
#     print(f"{k}: {v}")
#



#------------------------------------案例---------------------------------


dict1 = {}


while True:
    print("-------------1.添加购物车")  #
    print("-------------2.修改购物车")  #
    print("-------------3.删除购物车")  #
    print("-------------4.查询购物车")  #
    print("-------------5.退出购物车")  #

    print("********请选择功能:")
    mode = input()
    match mode:
        case "1":
            name = input("请输入商品名称:")
            price = input("请输入商品价格:")
            amount = input("请输入商品数量数量:")
            dict1[name] = [price,amount]
            continue
        case "2":
            print(dict1)
            name = input("请输入商品名称:")
            dict1[name][0] =input("请输入商品新价格:")
            dict1[name][1] =input("请输入商品新数量:")
            continue
        case "3":
            print(dict1)
            name = input("请输入商品名称:")
            del dict1[name]
            continue
        case "4":
            print("名称\t\t单价\t\t数量\t\t")
            for i in dict1.keys():
                print(f"{i}\t\t{dict1[i][0]}\t\t{dict1[i][1]}")
        case "5":
            break
        case _:
            print("输入非法")












