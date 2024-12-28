# 在python中，如果希望实现文件管理操作，需要使用OS模块

# 文件操作：
#   rename  用法：重命名文件    示例：os.rename("源文件名", "目标文件名")
#   remove  用法：删除文件      示例：os.remove("文件名")
# 目录操作：
#   listdir     目录列表        os.listdir("目录名")
#   mkdir       创建目录        os.mkdir("目录名")
#   rmdir       删除目录        os.rmdir("目录名")
#   getcwd      获取当前目录    os.getcwd()
#   chdir       修改工作目录    os.chdir("目标目录")
#   path.isdir  判断是否文件    os.path.isdir("文件路径")

# 提示：文件或者目录都支持相对路径和绝对路径

import os
print(os.getcwd())  # 打印输出当前所在目录
