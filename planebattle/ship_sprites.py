import random
import pygame
# 设置屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 480)
# 设置刷新帧率
FRAME_PER_SEC = 60
# 创建敌人
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 子弹时间
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed


    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprite):
    def __init__(self,is_alt= False):
        super().__init__(".\image\\a.jpg")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        # 调用父类，创建敌机精灵和图片
        super().__init__(".\image\enemy.png")
        # 随机敌机位置
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        self.rect.bottom = 0
        # 敌机随机速度
        self.speed = random.randint(1, 6)
        self.bullets_group = pygame.sprite.Group()

    def fire(self):
        print("发射...")
        # 定义子弹位置和子弹精灵组
        bullet = Bullet()
        for i in (0, 1, 2):
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.y = self.rect.y + i * 5
            self.bullets_group.add(bullet)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            print("将敌机删除")
            self.kill()

    def __del__(self):
        print("敌机被删除了..%s" % self.rect)


class Hero(GameSprite):
    """"英雄类"""
    def __init__(self):
        # 定义英雄图片和速度
        super().__init__(".\image\plane.png", 0)
        # 定义初始英雄位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.height-50
        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        if True:
            self.rect.x += self.speed
        else:
            self.rect.y += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射...")
        # 定义子弹位置和子弹精灵组
        bullet = Bullet()
        for i in (0,1,2):
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.y = self.rect.y - i*5
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__(".\image\\bullet.png", -4)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被删除了..")