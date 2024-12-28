class demo:
    instance = False    # 记录是否执行过初始化动作
    def __init__(self) -> None:
        if demo.instance == False:
            print("进行初始化")
        demo.instance = True    # 修改类属性

a = demo()
b = demo()  # 初始化方法只会执行一次