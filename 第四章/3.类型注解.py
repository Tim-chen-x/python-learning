# # 没有类型注解  ------>会有类型推断
# a = 100
# score = 98.5
# hobby = "python"
# flag = True
# pic = None
#
# names = ["A","B","C","D","E","F","G","H","I"]
# phones = ["19037372970","19507492473"]
# options = {"count":2,"total":10}
# goods = ("手机",6999,1)
#
# names.append("X")
# names.append(100010)
# print(names)
#
#
# # 变量定义 - 指定类型注解
# a2: int = 677
# score2: float = 98.5
# hobby2: str = "python"
# flag2: bool = True
# pic2: None = None
#
# names2: list[str] = ["A","B","C","D","E","F","G","H","I"]
# phones2: list[str] = ["19037372970","19507492473"]
# options2: dict[str,int] = {"count":2,"total":10}
# goods2: tuple[str,int,int] = ("手机",6999,1)
#
# names2.append(100.0)   #只是起到提示作用，也可以添加和输出。如果不进行类型注解，python也会有类型推断，同样会提示
# print(names2)


def calc_data(*args: int) -> float:
    return max(args)
print(calc_data(10,8,9))

def calc_data1(scores: list[int]) -> tuple[int,int,float]:
    return max(scores),min(scores),sum(scores)/len(scores)
print(calc_data1([1,2,3,4,45]))

def calc_data2(*args: int) -> tuple[int,int,float]:
    print(args)
    return max(args),min(args),sum(args)/len(args)
print(calc_data2(1,2,3,4,45))

#注意区分calc_data1和calc_data2: 1需要传入的参数是一个列表（要有中括号），2传入的是不定长参数，在进行类型注解的时候，
#--------int是指*args这个元组里面每一个元素的类型，这个元素可以还是元组（嵌套元组）


