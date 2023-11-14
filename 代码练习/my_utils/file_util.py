def print_file_info(file_name):
    """
    将给定的文件路径输出到控制台
    :param file_name: 文件路劲
    :return: 文件内容
    """
    f = None
    try:
        f = open(file_name, mode='r', encoding='utf-8')
        print("文件的全部内容如下：")
        print(f.read())
    except Exception as e:
        print("程序出现异常了，原因如下：")
        print(e)
    finally:
        # 如果异常就不用关闭
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    将data数据写入到file——name的路径中
    :param file_name:文件路径
    :param data:要写入的数据
    :return:写入完成后的数据
    """
    f = open(file_name, mode='a', encoding='utf-8')
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    # print_file_info("D:/代码仓库/Python/代码练习/my_utils/test.txt")
    append_to_file("D:/代码仓库/Python/代码练习/my_utils/test1.txt", "去死吧，我才不喜欢你！！！")
