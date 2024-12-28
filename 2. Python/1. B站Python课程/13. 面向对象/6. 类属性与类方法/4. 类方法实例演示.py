# 示例需求：
#   定义一个工具类
#   每件工具都有一个自己的name
#   需求--在类中封装一个show_tool_count的类方法，输出使用当前这个类创建的对象个数

class Tool:
    count = 0
    def __init__(self, name) -> None:
        Tool.count += 1
        name = name
    @classmethod
    def show_tool_count(cls):
        print(cls.count)


tool1 = Tool("t1")
tool2 = Tool("t2")
tool3 = Tool("t3")
tool4 = Tool("t4")
Tool.show_tool_count()