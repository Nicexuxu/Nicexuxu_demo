import pygame

# 坐标系：
#   x轴水平方向向右，逐渐增加
#   y轴竖直方向向下，逐渐增加
# 在游戏中，所有可见的元素都是以矩形区域来描述位置的
# 描述一个矩形区域的：四要素(x, y)(width, height)

# pygame专门提供了一个类pygame.Rect用于描述矩形区域!!
# Rect(x, y, width, height) -> Rect
#       pygame.Rect
#       x, y,
#       left, top, bottom, right,
#       center, centerx, centery,
#       size, width, height

# pygame.Rect是一个比较特殊的类，内部只是封装了一些数字计算
# 不执行pygame.init()方法同样能够使用 (init主要是针对窗口和图像绘制进行初始化的)
 
hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height))
print(hero_rect.size)       # size可以返回width和height
