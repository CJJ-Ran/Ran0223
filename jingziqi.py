# -*- coding:utf8 -*-
import pygame
import sys
import time
from random import *

pygame.init()
screen = pygame.display.set_mode([421, 450])  # 定义屏幕尺寸
pygame.display.set_caption('井字棋')
screen.fill([255, 255, 255])  # 定义屏幕底色


def menus(x, y, z, f=20):  # 显示需要的文字
    font = pygame.font.Font('simkai.ttf', f)
    set = font.render(x, 1, (0, 0, 0))
    textpos = [y, z]
    screen.blit(set, textpos)


def chessboard():  # 画出棋盘
    for i in range(0, 560, 140):
        pygame.draw.line(screen, [255, 0, 0], [i, 0], [i, 420])
        for j in range(0, 580, 140):
            pygame.draw.line(screen, [255, 0, 0], [0, j], [420, j])


def draw_x(x, y):  # 画叉
    pygame.draw.line(screen, [0, 255, 0], [x * 140 + 30, y * 140 + 30], [x * 140 + 110, y * 140 + 110], 10)
    pygame.draw.line(screen, [0, 255, 0], [x * 140 + 30, y * 140 + 110], [x * 140 + 110, y * 140 + 30], 10)


def draw_o(x, y):  # 画圆
    pygame.draw.circle(screen, [255, 0, 100], [x * 140 + 70, y * 140 + 70], 50, 10)


def draw_rect(lst, G=0, weight=2): # 画长方形，用来覆盖需要覆盖的地方
    pygame.draw.rect(screen, [255, G, 255], lst, weight)


def play_decide(game):      # 判断输赢
    if 5 in game:
        if (4 in game and 6 in game) or (2 in game and 8 in game) or (1 in game and 9 in game) or (
                3 in game and 7 in game):
            return True
    if 1 in game:
        if (2 in game and 3 in game) or (4 in game and 7 in game):
            return True
    if 9 in game:
        if (3 in game and 6 in game) or (7 in game and 8 in game):
            return True


def Zero():   # 给井字棋的9个格分别用数字打上标签
    label = 0
    zero = []
    for i in range(3):
        for j in range(3):
            label += 1
            zero.append([i, j, label])
    return zero


choose = {
    1: [19, 424, 61, 22],
    2: [99, 424, 81, 22],
    3: [199, 424, 81, 22],
    4: [299, 424, 41, 22],
    5: [359, 424, 21, 22],
    6: [389, 424, 21, 22],
}       #   菜单位置
menu = {
    u'新游戏': 20,
    u'人人对战': 100,
    u'人机对战': 200,
    u'悔棋': 300,
    'X': 365,
    'O': 395,
}   # 菜单文字
chessboard()  # 画出棋盘
for i in choose.values():
    draw_rect(i)
for i in menu.keys():
    menus(i, menu[i], 425)
pygame.display.flip()  # 刷新屏幕
game_data = Zero()
game_X = []
game_O = []
X_decide = False
O_decide = False
All_decide = True
game_num = 0
ren_ren = False
ren_ji = False
com_nochoose = []
while True:
    x_pos = pygame.mouse.get_pos()[0] / 140
    y_pos = pygame.mouse.get_pos()[1] / 140
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(99, 180) and event.pos[1] in range(424, 446):
            ren_ren = True
            ren_ji = False      #   选择人人模式
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(199, 280) and event.pos[1] in range(424, 446):
            ren_ren = False
            ren_ji = True       #   选择人机模式
        if ren_ren:             # 人人模式
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(359, 380) and event.pos[1] in range(424, 446):
                X_decide = False    # 选择O棋子
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(359, 380) and event.pos[1] in range(424, 446):
                X_decide = True     # 选择X棋子
            if X_decide :           # 游戏时交替判断该谁下棋
                O_decide = False
            else:
                O_decide = True
            if event.type == pygame.MOUSEBUTTONDOWN and \
                            event.pos[0] in range(0, 420) and \
                            event.pos[1] in range(0, 420) and X_decide and All_decide:    #  在有效区域内点击下棋
                game_num += 1
                draw_x(x_pos, y_pos)
                pygame.display.flip()
                if [x_pos, y_pos] in [i[:2] for i in game_data]:
                    decide_x = True
                    count_x = 0
                    while decide_x:
                        if [x_pos, y_pos] == game_data[count_x][:2]:
                            game_X.append(game_data[count_x][-1])
                            decide_x = False
                        count_x += 1
                    play_decide(game_X)
                    if play_decide(game_X):
                        All_decide = False
                        draw_rect([120, 160, 180, 101], G=100, weight=0)
                        menus("X WIN", 135, 180, 60)
                        pygame.display.flip()
                X_decide = False
            if event.type == pygame.MOUSEBUTTONDOWN and \
                            event.pos[0] in range(0, 420) and \
                            event.pos[1] in range(0, 420) and O_decide and All_decide:
                game_num += 1
                draw_o(x_pos, y_pos)
                pygame.display.flip()
                if [x_pos, y_pos] in [i[:2] for i in game_data]:
                    decide_o = True
                    count_o = 0
                    while decide_o:
                        if [x_pos, y_pos] == game_data[count_o][:2]:
                            game_O.append(game_data[count_o][-1])
                            decide_o = False
                        count_o += 1
                    play_decide(game_O)
                    if play_decide(game_O):
                        All_decide = False
                        draw_rect([120, 160, 180, 101], G=100, weight=0)
                        menus("O WIN", 135, 180, 60)
                        pygame.display.flip()
                X_decide = True
            if game_num == 9:
                All_decide = False
                draw_rect([120, 160, 180, 101], G=100, weight=0)
                menus(u"平 局", 135, 180, 60)
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and \
                            event.pos[0] in range(20, 80) and event.pos[1] in range(425, 445):
                draw_rect([0, 0, 420, 421], G=255, weight=0)
                chessboard()
                pygame.display.flip()
                X_decide = False
                O_decide = False
                All_decide = True
                game_data = Zero()
                game_X = []
                game_O = []
                game_num = 0
                ren_ren = False
        if ren_ji:      #   人机模式
            if event.type == pygame.MOUSEBUTTONDOWN and \
                            event.pos[0] in range(0, 420) and \
                            event.pos[1] in range(0, 420) and All_decide:
                game_num += 1
                draw_x(x_pos, y_pos)
                pygame.display.flip()
                if [x_pos, y_pos] in [i[:2] for i in game_data]:
                    decide_x = True
                    count_x = 0
                    while decide_x:
                        if [x_pos, y_pos] == game_data[count_x][:2]:
                            game_X.append(game_data[count_x][-1])
                            com_nochoose = game_data
                            com_nochoose.pop(count_x)
                            decide_x = False
                        count_x += 1
                    play_decide(game_X)
                    if play_decide(game_X):
                        All_decide = False
                        draw_rect([120, 160, 180, 101], G=100, weight=0)
                        menus("X WIN", 135, 180, 60)
                        X_decide = True
                        pygame.display.flip()
                if not X_decide:
                    time.sleep(2)
                    game_num += 1
                    com_choose = choice(com_nochoose)
                    draw_o(com_choose[0], com_choose[1])
                    com_nochoose.remove(com_choose)
                    pygame.display.flip()
                    game_O.append(com_choose[-1])
                    play_decide(game_O)
                    if play_decide(game_O):
                        All_decide = False
                        draw_rect([120, 160, 180, 101], G=100, weight=0)
                        menus("O WIN", 135, 180, 60)
                        pygame.display.flip()
            if game_num == 9:
                All_decide = False
                draw_rect([120, 160, 180, 101], G=100, weight=0)
                menus(u"平 局", 135, 180, 60)
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and \
                            event.pos[0] in range(20, 80) and event.pos[1] in range(425, 445):      #   新游戏
                draw_rect([0, 0, 420, 421], G=255, weight=0)
                chessboard()
                pygame.display.flip()
                X_decide = False
                O_decide = False
                All_decide = True
                game_data = Zero()
                game_X = []
                game_O = []
                game_num = 0
                ren_ji = False
                com_nochoose = []
