# 游戏初始化：
#   设置游戏窗口
#   绘制图像初始位置
#   设置游戏时钟
# 游戏循环：
#   设置刷新率
#   检测用户交互
#   更新所有图像位置
#   更新屏幕显示



# 游戏初始化：
import pygame 
pygame.init()
screen = pygame.display.set_mode((480, 700))        # 创建窗口
bg = pygame.image.load("../images/background.png")  # 加载背景
screen.blit(bg, (0, 0))                             # 显示背景
# 要在屏幕上显示图像，需要按照三个步骤：
#   1. 使用pygame.image.load()加载图像数据到内存
#      load(file_path)
#   2. 使用游戏屏幕对象，调用blit方法将图像绘制到指定位置
#      blit(图像，位置)
#   3. 调用pygame.display.update()方法更新整个屏幕的显示
#      pygame.display.update()
# 绘制英雄的飞机
hero = pygame.image.load("../images/me1.png")   # 加载到内存
screen.blit(hero, (190, 500))       # 把hero显示到屏幕上
pygame.display.update()         # 统一刷新屏幕



# pygame专门提供了一个类pygame.time.Clock可以非常方便地设置屏幕绘制速度
# tick方法会根据上次被调用的实践，自动设置游戏循环中的延时
# 要使用时钟对象需要两步：
#   1. 在游戏初始化创建一个时钟对象
#   2. 在游戏循环中让时钟对象调用tick(帧率方法)
clock  = pygame.time.Clock()    # 创建时钟对象

# 游戏循环
while True:
    clock.tick(1)               # 时钟对象调用tick方法，设置游戏刷新率
    

pygame.quit()