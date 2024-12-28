# python创建类时可以继承父类的方法和属性
# class 子类(父类):  用于继承

class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def jump(self):
        print("跳")


class Dog(Animal):  # 只继承，啥也不做
    pass

dog = Dog()         # 用子类创建对象，依旧能够调用父类的方法
dog.eat()
dog.drink()
dog.run()
dog.jump()

# 专业术语：
# Dog类是Animal类的子类，Animal类是Dog类的父类，Dog类从Animal类继承
# Dog类是Animal类的派生类，Animal类是Dog类的基类，Dog类从Animal类派生

# 类的继承可传递
class Dog2(Dog):
    pass
class Dog3(Dog2):
    pass
ceshi = Dog3()
ceshi.eat()
ceshi.drink()
ceshi.run()
ceshi.jump()