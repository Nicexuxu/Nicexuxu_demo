# 小文件复制
# 1. 打开文件
file_read = open("DEMO3.txt", encoding="utf-8")
file_write = open("DEMO3_copy.txt", "w", encoding="utf-8")  # 不存在会创建

# 2. 读，写
text = file_read.read()
file_write.write(text)

# 3. 关闭别忘了
file_read.close()
file_write.close()