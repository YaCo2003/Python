# 嵌套语句
if int(input("请输入你的身高 ")) > 120:
    print("身高超出限制")
    print("但是如果vip等级大于3，可以免费")
    if int(input("请输入VIP等级：")) > 3:
        print("可以免费玩")
    else:
        print("需要补10元票")
else:
    print("儿童免费")
print("祝你玩得愉快")
