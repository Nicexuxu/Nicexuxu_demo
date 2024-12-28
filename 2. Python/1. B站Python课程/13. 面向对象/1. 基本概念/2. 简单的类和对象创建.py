class Cat():            # 大驼峰命名法
    def eat(self):      # 方法后面括号一定要加self
        print("吃吃吃")
    def drink(self):
        print("喝喝喝")
    def printself(self):
        print(self.name)

tom = Cat()         # 创建猫对象
tom.eat()
tom.drink()


# 在面向对象的开发过程中，引用的概念是同样适用的

print(tom)              # 直接print可以输出对象在内存中的信息
print(id(tom))
print("%x" % id(tom))   # %d可以十进制输出数字，%s可以十六进制输出数字


# 对象.属性名=名 可以为对象创建一个属性（破坏了类的完整性，不推荐，会报红）
tom.name = "Tom"
print(tom.name)


# 封装类def的函数括号后面的self即代表对象本身
tom.printself()