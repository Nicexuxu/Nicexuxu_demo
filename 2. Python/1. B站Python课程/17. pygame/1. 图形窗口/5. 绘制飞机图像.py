import pygame 
pygame.init()

screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load("../images/background.png")
screen.blit(bg, (0, 0))

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





while True:
    pass
pygame.quit()