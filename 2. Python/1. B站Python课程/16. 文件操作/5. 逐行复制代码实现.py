# 小文件复制
# 1. 打开文件
file_read = open("DEMO4.txt", encoding="utf-8")
file_write = open("DEMO4_copy.txt", "w", encoding="utf-8")  # 不存在会创建

# 2. 读，写
while True:
    text = file_read.readline() # 每次读取一行，指针放在结尾
    if not text:            # 读取完才break
        break
    file_write.write(text)  # 每次写入一行，指针放在结尾

# 3. 关闭别忘了
file_read.close()
file_write.close()