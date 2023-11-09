# 1、接收
# mylist = [21, 25, 21, 23, 22, 20]
# print(mylist)
# # 2、追加31
# mylist.append(31)
# print(mylist)
# # 3、追加列表 [29,33,30]
# list1 = [29, 33, 30]
# mylist.extend(list1)
# print(mylist)
# # 4、取出第一个元素
# print(mylist.pop(0))
# print(mylist)
# # 5、取出最后一个元素
# print(mylist.pop(-1))
# print(mylist)
# # 6、查找元素31，在列表下标位置
# x = mylist.index(31)
# print(f"元素31在列表的下表为{x}")

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist1 = []
mylist2 = []

def func_while(mylist):
    x = 0
    while x < len(mylist):
        if mylist[x] % 2 == 0:
            mylist1.append(mylist[x])
        x+=1
    print(f"通过while循环，从列表：{mylist}中取出偶数，组成新列表{mylist1}")



def func_for(mylist):
    for x in mylist:
        if x % 2 == 0:
            mylist2.append(x)
    print(f"通过for循环，从列表：{mylist}中取出偶数，组成新列表{mylist2}")


func_while(mylist)
func_for(mylist)
