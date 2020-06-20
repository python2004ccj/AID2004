"""
 3. 现在有两个文本文件（自己指定），编写一个程序，将两个文件合并为一个

"""


def amalgamate(file01, file02):
    """
    思想：先读取第一个文本文件,同时写入新文本文件中,读取写入完后调用函数读取写入第二个文本文件
    :param file01:
    :param file02:
    :return:
    """
    fr1 = open(file01, "r")
    fw = open("file_w.txt", "a")
    while True:
        data_fr1 = fr1.read(1024 * 1024)
        if not data_fr1:
            write_fr2(file02, fw)
            break
        fw.write(data_fr1)


def write_fr2(file02, fw):
    fr2 = open(file02, "r")
    while True:
        data_fr2 = fr2.read(1024 * 1024)
        if not data_fr2:
            break
        fw.write(data_fr2)
    fr2.close()


if __name__ == '__main__':
    file01 = "file01.txt"
    file02 = "file02.txt"
    amalgamate(file01, file02)
