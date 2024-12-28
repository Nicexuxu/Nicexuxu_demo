class Gun:
    def __init__(self, model) -> None:
        self.model = model
        self.bullet_count = 0
    
    def add_bullet(self, count):
        self.bullet_count += count
        print("装填后有%s发子弹" % self.bullet_count)

    def shoot(self):
        if self.bullet_count < 1:
            print("子弹不足")
            return
        self.bullet_count -= 1
        print("%s突突突，发射了一发子弹，还剩下%s发" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name) -> None:
        self.name = name
        self.gun = None
    def fire(self):
        if self.gun is None:            # 判断是否等于None推荐使用is
            print("没有枪")
            return
        print("冲冲冲")
        self.gun.add_bullet(20)
        self.gun.shoot()
        


ak47 = Gun("AK47")
xusanduo = Soldier("士兵")
xusanduo.gun = ak47                 # type:ignore
xusanduo.fire()
print(xusanduo.gun)