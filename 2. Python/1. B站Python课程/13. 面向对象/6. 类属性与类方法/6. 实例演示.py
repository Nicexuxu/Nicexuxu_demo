# 需求：
#   设计一个Game类
# 属性：
#   定义一个类属性top_score记录游戏的历史最高分
#   定义一个实例属性player_name记录当前游戏的玩家姓名
# 方法：
#   静态方法show_help显示游戏帮助信息
#   类方法show_top_score显示历史最高分
#   实例方法start_game开始当前玩家的游戏
# 主程序步骤：
#   查看帮助信息
#   查看历史最高分
#   创建游戏对象，开始游戏

class Game:
    top_score = 0
    
    def __init__(self, name) -> None:   # 初始化方法设置实例的名字属性
        self.player_name = name
    
    @staticmethod
    def show_help():                    # 静态方法 打印帮助信息
        print("别让僵尸进入房子")
    
    @classmethod
    def show_top_score(cls):            # 类方法 打印类的得分属性信息
        print(cls.top_score)

    def start_game(self):               # 实例方法 开始游戏 访问到实例的名字属性
        print("%s，游戏开始了" % self.player_name)


Game.show_help()                        # 静态方法和类方法通过类名调用
Game.show_top_score()                   # 静态方法和类方法通过类名调用
game = Game("小明")                     # 先创建实例
game.start_game()                       # 调用实例方法