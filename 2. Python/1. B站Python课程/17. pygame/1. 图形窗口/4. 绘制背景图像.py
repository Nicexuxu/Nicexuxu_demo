import pygame 
pygame.init()

screen = pygame.display.set_mode((480, 700))

# 要在屏幕上显示图像，需要按照三个步骤：
#   1. 使用pygame.image.load()加载图像数据到内存
#      load(file_path)
#   2. 使用游戏屏幕对象，调用blit方法将图像绘制到指定位置
#      blit(图像，位置)
#   3. 调用pygame.display.update()方法更新整个屏幕的显示
#      pygame.display.update()

# 1. 加载图像
bg = pygame.image.load("../images/background.png")
# 2. 绘制图像
screen.blit(bg, (0, 0))
# 3. 更新屏幕显示
pygame.display.update()



while True:
    pass
pygame.quit()