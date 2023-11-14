# def func(a,b):
# from time import sleep
# sleep(11)

# import 循环
import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("黑马程序员", 2, 4))

file_util.print_file_info("D:/代码仓库/Python/代码练习/my_utils/test1.txt")
file_util.append_to_file("D:/代码仓库/Python/代码练习/my_utils/test1.txt", "讨厌死了")
file_util.print_file_info("D:/代码仓库/Python/代码练习/my_utils/test1.txt")
