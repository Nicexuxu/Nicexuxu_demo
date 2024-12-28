# 在python中要操作文件需要记住1个函数和3个方法

'''
1:  open    打开文件，并且返回文件操作对象  文件名区分大小写
2.  read    将文件内容读取到内存    注意！！ read方法执行后指针会移动到文件的末尾
3.  write   将指定内容写入文件
4.  close   关闭文件
'''

file = open("DEMO.txt", encoding="utf - 8") # windows中文系统默认使用gbk，打开的时候要指定utf-8
print(file.read())
file.close()