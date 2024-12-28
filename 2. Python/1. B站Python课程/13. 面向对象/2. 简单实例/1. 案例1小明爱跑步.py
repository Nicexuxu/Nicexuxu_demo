# 需求：小明体重75kg，跑步减肥0.5kg，吃饭增加1kg

class person:
    def __init__(self, name, weight) -> None:           # 定义name和weight属性，由调用时传入
        self.name = name
        self.weight = weight
    def __str__(self) -> str:
        return "我是%s, 我的体重%s" % (self.name, self.weight)
    def eat(self):                                      # 吃，体重+1
        self.weight += 1
    def run(self):                                      # 跑，体重-0.5
        self.weight -= 0.5
xiaoming = person("xiaoming", 80)
print(xiaoming)
xiaoming.eat()
xiaoming.run()
print("我是%s，在经过一些活动后，我的体重是%d" % (xiaoming.name, xiaoming.weight))

# 拓展：再创建新对象不会影响原有对象
xiaomei = person("小美", 50)
print(xiaomei)