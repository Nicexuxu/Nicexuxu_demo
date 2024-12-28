# read方法默认会把文件的所有内容一次性读取到内存
# 如果文件太大，堆内存的占用会非常严重
# readline方法：
#   readline方法可以一次读取一行内容
#   方法执行后，会把文件指针移动到下一行，准备再次读取

# 读取大文件的正确方法：
# 打开文件
file = open("DEMO2.txt", encoding = "utf-8")

while True:
    # 读取一行内容
    text = file.readline() # 每次执行后指针都会移动到下一行

    # 判断是否读到内容
    if not text:    # 空字符串为False
        break

    # 每读取一行的末尾已经有了一个'\n'
    print(text, end="")

file.close()  # 文件别忘了关闭