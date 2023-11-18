# def func(a,b):
# from time import sleep
# sleep(11)

# import 循环
import 代码练习.第一阶段.my_utils.str_util
from 代码练习.第一阶段.my_utils import file_util

print(代码练习.第一阶段.my_utils.str_util.str_reverse("黑马程序员"))
print(代码练习.第一阶段.my_utils.str_util.substr("黑马程序员", 2, 4))

file_util.print_file_info("/代码练习/第一阶段/my_utils/test1.txt")
file_util.append_to_file("/代码练习/第一阶段/my_utils/test1.txt", "讨厌死了")
file_util.print_file_info("/代码练习/第一阶段/my_utils/test1.txt")
