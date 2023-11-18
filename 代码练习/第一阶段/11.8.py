# name="ithema"
# for x in name:
#     print(x)

# name = "itheima is a brand of itcast"
# cnt = 0
# for x in name:
#     if x == 'a':
#         cnt += 1
# print(f"itheima is a brand of itcast中共含有：{cnt}个字母a")
# num = 10
# cnt=0
# for x in range(1,num) :
#     if x%2==0:
#         cnt+=1
# print(f"从1到{num},一共有{cnt}个偶数")
sum=10000
for i in range(1,21):
    #随机生成绩效
    import random
    num = random.randint(1, 10)
    if num<5:
        print(f"员工{i}，绩效分为{num}，低于5，不发工资，下一位。")
    else:
        sum-=1000
        print(f"向员工{i}发放工资1000元,账户余额还剩余{sum}元")
        if sum<=0:
            print("工资发完了，下个月领取吧")
            break