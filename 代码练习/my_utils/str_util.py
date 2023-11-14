def str_reverse(s):
    """
    将字符串反转
    :param s:输入字符串
    :return:反转字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    字符串切片
    :param s: 被切片的字符串
    :param x:开始下表
    :param y:结束下表
    :return:切片完成的字符串
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse("world"))
    print(substr("hello", 2, 4))