from ship_sprites import *
import pygame


class PlaneGame(object):
    def __init__(self):

        print('游戏初始化')
    # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
    # 创建游戏时钟
        self.clock = pygame.time.Clock()
    # 调用私有方法，创建精灵和精灵组
        self.__create_sprites()
    # 设置定时器时间，频率
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵
        self.enemy = Enemy()
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")
        while True:
            # 设置刷新帧
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handle()
            # 碰撞检测
            self.__check_collide()
            # 精灵组的更新
            self.__update_sprites()
            # 绘制图形
            pygame.display.update()

    def __event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

           # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
               # print("向右移动..")
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_RIGHT]:
            self.hero.speed = 5
        elif key_press[pygame.K_LEFT]:
            self.hero.speed = -5
        elif key_press[pygame.K_UP]:
            self.hero.speed = -2
            flag = 1
        elif key_press[pygame.K_DOWN]:
            self.hero.speed = 2
            flag = 1
        else:
            self.hero.speed = 0


    def __check_collide(self):
        # 精灵组之间碰撞检测
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        # 精灵与精灵组碰撞
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()

            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

        self.enemy.bullets_group.update()
        self.enemy.bullets_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()

    game.start_game()

