
money=50000;# 余额
name=None
#查询函数
def check(bo):
    if bo:
        print("----------查询余额----------")
    print(f"{name}，您好，您的余额剩余{money}")
# 存款
def deposit(x):
    global money
    money += x
    print("------------存款------------")
    print(f"{name}，您好，您存款{x}成功")
    check(False)
#取款
def take(x):
    global money
    print("------------取款------------")
    if (money - x)<=0:
        print("对不起，您的余额不足")
        check(False)
    else:
        print(f"{name}，您好，您取款{x}元成功")
        money -= x
        check(False)


def menu():
    print("----------主菜单----------")
    print(f"{name}，您好，欢迎来到银行，请选择你的操作")
    print("查询余额\t【输入1】")
    print("存款\t【输入2】")
    print("取款\t【输入3】")
    print("退出\t【输入4】")
    return input("请输入您的选择：")


name=input('请输入您的姓名：')
while 1:
    x=menu()
    if x=="1":
        check(True)
    elif x=="2":
        deposit(int(input("请输入存款金额：")))
    elif x=="3":
        take(int(input("请输入取款金额：")))
    else:
        print("欢迎您下次光临！")
        break;

