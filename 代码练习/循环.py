
# cnt=1
# i=0
# while cnt<=100:
#     print("第%s次相加"%cnt)
#     i += cnt
#     cnt+=1
#
#
# print("1累加到100的和为：%s"%i)
# 随即猜数字

import random
num=random.randint(1,100)
print(num)
bool_guess=True
cnt=1
while bool_guess:
    guess_num = int(input(f"第{cnt}次猜数字："))
    if guess_num==num:
        print(f"恭喜你，第{cnt}次猜对了")
        bool_guess=False
    else:
        if guess_num>num:
            print("猜大了")
        else:
            print("猜小了")
    cnt+=1


