# 需求：定义一个数字 1-10随机产生，通过三次判断猜出来数字

import random
num = random.randint(1, 10)
print(num)

guess_num=int(input("第一次猜数字："))

if guess_num==num:
    print("恭喜你猜对了")
else:
    if guess_num > num:
        print("猜大了")
    else:
        print("猜小了")

    guess_num = int(input("第二次猜数字："))
    if guess_num==num:
        print("恭喜你第二次猜对了")
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")

        guess_num = int(input("第三次猜数字："))
        if guess_num == num:
            print("恭喜你第三次猜对了")
        else:
            print("猜错了，游戏结束")
