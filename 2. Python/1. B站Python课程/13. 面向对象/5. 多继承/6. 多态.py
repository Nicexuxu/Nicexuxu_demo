# 多态：不同的子类对象调用相同的办法产生不同的结果

class Dog(object):
    def __init__(self, name) -> None:
        self.name = name
    
    def game(self):
        print(self.name, "玩游戏，汪汪叫")



class XiaoTianQuan(object):
    def __init__(self, name) -> None:
        self.name = name
        
    def game(self):
        print(self.name, "哮天犬玩游戏，汪汪叫")


class Person(object):
    def __init__(self, name) -> None:
        self.name = name

    def game(self, dog):
        print("人和%s一起玩游戏" % dog.name)
        dog.game()


wangcai = Dog("旺财")
xiaotianquanwangcai = XiaoTianQuan("哮天犬旺财")
xm = Person("小明")
xm.game(wangcai)                # 不同的子类对象调用相同的办法产生不同的结果
xm.game(xiaotianquanwangcai)    # 不同的子类对象调用相同的办法产生不同的结果