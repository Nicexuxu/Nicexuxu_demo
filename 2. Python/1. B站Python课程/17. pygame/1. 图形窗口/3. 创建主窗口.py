import pygame
pygame.init()

# pygame专门提供了一个模块pygame.display用于创建、管理游戏窗口
#   pygame.display.set_mode()     初始化游戏显示窗口
#   pygame.display.update()       刷新屏幕内容显示


# set_mode方法：
#   set_mode(resolution=(0,0), flags=0, depth=0) -> Surface
#   resolution指定屏幕的宽和高，默认创建的大小和屏幕大小一致
#   flags参数指定屏幕的附加选项，比如是否全屏等等，默认不需要传递
#   depth参数表示颜色的位数，默认自动匹配
screen = pygame.display.set_mode((480, 700))    # 创建一个480x700的窗口
while True:                                     # 循环使python一直运行，保持住窗口
    pass

pygame.quit()