import pygame

from ship_sprites import *


pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480, 480))
# 加载图片
ship = pygame.image.load("F:\PythonTest\image\ship.bmp")
background = pygame.image.load("F:\PythonTest\image\img_bg.jpg")
screen.blit(ship, (240, 450))
screen.blit(background, (0, 0))
ship_rect = pygame.Rect(240, 450, 20, 24)
pygame.display.update()
# 设置游戏频率
clock = pygame.time.Clock()
# 创建游戏精灵
enemy = GameSprite("F:\PythonTest\image\img_enemy.bmp")
enemy2 = GameSprite("F:\PythonTest\image\img_enemy.bmp", 3)
# 创建游戏精灵组
enemy_group = pygame.sprite.Group(enemy, enemy2)
while True:

    clock.tick(60)
    ship_rect.y -= 2
    if ship_rect.y < 0:
        ship_rect.y = 450
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    screen.blit(ship, ship_rect)
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()

pygame.quit()