
# fr = open("file04.txt","r")
# data = fr.read()
# print(data)
# data = fr.read(20)
# print(data)
# data = fr.readline()
# print(data)
# data = fr.readlines(50)
# print(data)
# fr.close()
# fw = open("file05.txt","w")
# msg = "hello!Everyone.\n"
# count = fw.write(msg)
# print("写入了%d个字符"%count)
# list_msg = ["hello!","Everyone.","my name is chen"]
# count = fw.writelines(list_msg)
# fw.close()

# fa = open("file05.txt","a")
# count = fa.write("\n我正在使用a的打开方式追加信息．")
# print("我追加了%d个字符"%count)
# fa.close()

# with open("file05.txt","w") as fw:
#     fw.write("清空喽，重新写入啦！")

# fw = open("file05.txt","w",buffering=1)
# n = 0
# while True:
#     n+=1
#     fw.write("第%d次循环写入\n"%n)

# fw = open("file05.txt","a",buffering=10)
# n = 0
# while True:
#     n+=1
#     fw.write("第%d次循环写入\n"%n)

# fw = open("flie06.txt","wb+")
# count = fw.write("我正在练习偏移量".encode())
# print(count)
# fw.seek(0,0)
# data = fw.read()
# print(data)
# fw.close()

