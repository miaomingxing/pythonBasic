import pygame
import time
from pygame.locals import *
import random

def key_control(hero_temp):
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()

class Base(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)



class BasePlane(Base):
    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self, screen_temp, x, y, image_name)
        self.bullet_list = []  # 存储发射出去的子弹的引用

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():#判断子弹是否越界
                self.bullet_list.remove(bullet)

class BaseBullet(Base):
    def __init__(self,screen_temp, x, y, image_name):
        Base.__init__(self,screen_temp, x, y, image_name)

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 210, 700, "./feiji/hero1.png")

    def move_left(self):
        self.x -= 7

    def move_right(self):
        self.x += 7

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class EnemyPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, "./feiji/enemy0.png")
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.x += 3
        elif self.direction == "left":
            self.x -= 3

        if self.x > 430:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1,100)
        if random_num == 8 or random_num == 70:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))


class Bullet(BaseBullet):
    def __init__(self,screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+40, y-20, "./feiji/bullet.png")

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    def __init__(self,screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 29.5, y + 39.5, "./feiji/bullet1.png")

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False


def main():
    #1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,852),0,32)
    #2.创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")
    #3.创建一个飞机对象
    hero = HeroPlane(screen)
    #4.创建一个敌机
    enemy = EnemyPlane(screen)
    #把背景图片放在窗口中显示
    while True:
        #设定需要显示的背景
        screen.blit(background, (0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        #更新需要显示的内容
        pygame.display.update()
        key_control(hero)
        #延时，防止老电脑出现CPU飙升问题
        time.sleep(0.001)

if __name__ == '__main__':
      main()