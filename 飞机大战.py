
"""
关注“python趣味爱好者”微信公众号，
回复game1,game2,game3,game4获取飞机大战，贪吃蛇，接水果，生命游戏.....
创作方：python趣味爱好者，转载请标注来源。
游戏规则：
按上下左右键移动飞机，按空格键发射子弹
"""
import pygame
import sys
from pygame.locals import*
import numpy as np
from random import randint
pygame.init()

rect_width=10
size=width,height=300,500
COLOR=(0,225,0)#飞机的颜色
x_rect=int(width/rect_width)
y_rect=int(height/rect_width)#长宽格子有多个

speed=[1,0]
bg=(255,0,0)
bullet_color=(0,255,255)
enemy_color=(255,255,0)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("python趣味爱好者")
#font=pygame.font.Font(None,20)

bullet_speed=5#子弹的速度
font1 = pygame.font.SysFont('宋体', 30, True)
font_list = pygame.font.get_fonts()
#render(text, antialias, color, background=None)
surface1 = font1.render(u'当前得分', True, [255, 0, 0])


airplane=[[12,y_rect-5],[12,y_rect-4],[12,y_rect-3],[11,y_rect-3],[13,y_rect-3]]
enemy_heart=[[2,3],[4,5]]#对方飞机中心位置
enemy_all=[]#对方飞机占有的全部的点
bullet=[]#子弹占据的位置。

shoot_or=0
score=0
def get_enemy_pos(pos):#将对方的飞机占有的所有的点全部添加到enemy_all里面。
    enemy_all.append([pos[0],pos[1]])
    enemy_all.append([pos[0]-1,pos[1]])
    enemy_all.append([pos[0]+1,pos[1]])
    enemy_all.append([pos[0],pos[1]+1])
    enemy_all.append([pos[0],pos[1]+2])

def get_pos(pos):#将对方的飞机占有的所有的点全部添加到enemy_all里面。
    enemy1=[]
    enemy1.append([pos[0],pos[1]])
    enemy1.append([pos[0]-1,pos[1]])
    enemy1.append([pos[0]+1,pos[1]])
    enemy1.append([pos[0],pos[1]+1])
    enemy1.append([pos[0],pos[1]+2])
    return enemy1

    
def get_rect(row,column):#计算应该在哪里画方格，以右上角为点。
    x1=rect_width*row
    y1=rect_width*column

    return (x1,y1,rect_width,rect_width)

#pygame.draw.rect(screen,COLOR,get_rect(row,column),0)

def move_airplane(speed):#左右移动盘子。
    for i in airplane:
        i[0]=i[0]+speed[0]
        i[1]=i[1]+speed[1]
    speed=[0,0]
 
def shoot_enemy():#判断是否击中了敌人
    global score
    for i in enemy_heart:
        the_rect=get_pos(i)#得到这个敌人占据的所有的点
        for j in the_rect:
            if j in bullet:
                enemy_heart.remove(i)
                score+=30
            else:
                pass
            


def change_fruit(enemys):
    for i in enemys:
        if i[0]>y_rect:
            i[1]=6

def move_enemy(enemys):
    for i in enemys:
        i[1]=i[1]+2
        
def creat_enemy():
    enemy_heart.append([randint(1,x_rect-1),randint(-8,0)])
    

def draw_airplane():#画自己的飞机
    for i in airplane:
        pygame.draw.rect(screen,COLOR,get_rect(i[0],i[1]),0)

def draw_enemy(enemys):#画敌人的飞机
    for i in enemys:
        if i[0]>0 and i[0]<x_rect and i[1]>0 and i[1]<y_rect:
            pygame.draw.rect(screen,enemy_color,get_rect(i[0],i[1]),0)

def draw_bullet():#画出所有的子弹。
    for i in bullet:
        pygame.draw.rect(screen,bullet_color,get_rect(i[0],i[1]),0)

def shoot():#产生子弹，也就是开始射击。
    pos1=[airplane[0][0],airplane[0][1]-1]
    bullet.append(pos1)
    for i in bullet:#删除越界的子弹
        if i[1]<0:
            bullet.remove(i)




k=0
score=30
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                speed=[-1,0]
            if event.key==K_RIGHT:
                speed=[1,0]
            if event.key==K_UP:
                speed=[0,-1]
            if event.key==K_DOWN:
                speed=[0,1]
            if event.key==K_SPACE:
                shoot()
            if event.key==K_a:
                exit()
                #shoot_or=1#进行射击操作。

    k+=1
    enemy_all=[]
    for i in enemy_heart:
        get_enemy_pos(i)
    for i in bullet:
        i[1]-=bullet_speed
        


    shoot_enemy()#判断子弹是否能击中敌人
    if k>4:
        creat_enemy()
        k=0
    else:
        pass
    move_enemy(enemy_heart)
    move_airplane(speed)
    change_fruit(enemy_all)
    screen.fill(bg)
    
    draw_airplane()
    draw_enemy(enemy_all)
    screen.blit(surface1, [20, 20])
    draw_bullet()#将所有的子弹全部画出来

    screen.blit(font1.render(u'当前得分：%d' % score, True, [255, 0, 0]), [20, 20])

    pygame.display.update()

    pygame.display.flip()
    pygame.time.delay(180)

