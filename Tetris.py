# -*-coding:utf-8-*-
import random
import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([200, 440])
pygame.display.set_caption('俄罗斯方块')
screen.fill([0, 250, 154])
pygame.draw.rect(screen, [250, 228, 181], [200, 0, 360, 400], 0)


# 用来选择方块种类及旋转方块
def Block(x, y):
    All = {
    0 : [[(x, y), (x+20, y), (x, y-20), (x+20, y-20)]],
    1 : [
        [(x, y), (x-20, y), (x+20, y), (x+40, y)],
        [(x, y), (x, y-20), (x, y-40), (x, y-60)]
    ],
    2 : [
        [(x, y), (x+20, y), (x, y-20), (x, y-40)],
        [(x, y), (x-20, y), (x+20, y), (x+20, y-20)],
        [(x, y), (x, y-20), (x, y-40), (x-20, y-40)],
        [(x, y), (x, y-20), (x+20, y-20), (x+40, y-20)]
    ],
    3 : [
        [(x, y), (x+20, y), (x+20, y-20), (x+20, y-40)],
        [(x, y), (x, y-20), (x-20, y-20), (x-40, y-20)],
        [(x, y), (x, y-20), (x, y-40), (x+20, y-40)],
        [(x, y), (x, y-20), (x+20, y), (x+40, y)]
    ],
    4 : [
        [(x, y), (x+20, y), (x, y-20), (x-20, y-20)],
        [(x, y), (x, y-20), (x+20, y-20), (x+20, y-40)]
    ],
    5 : [
        [(x, y), (x-20, y), (x, y-20), (x+20, y-20)],
        [(x, y), (x, y-20), (x-20, y-20), (x-20, y-40)]
    ],
    6 : [
        [(x, y), (x, y-20), (x-20, y-20), (x+20, y-20)],
        [(x, y), (x, y-20), (x, y-40), (x+20, y-20)],
        [(x, y), (x-20, y), (x+20, y), (x, y-20)],
        [(x, y), (x, y-20), (x-20, y-20), (x, y-40)]
    ]
}
    return All


# 画方格
def ChessBoard():
    for i in range(20, 420, 20):
        pygame.draw.line(screen, [250, 228, 181], [0, i], [200, i])
        for j in range(20, 200, 20):
            pygame.draw.line(screen, [250, 228, 181], [j, 0], [j, 400])


# 显示文字
def Score(x, y, z):
    font = pygame.font.Font(None, 35)
    set = font.render(x, 1, (0, 0, 0))
    textpos = [y, z]
    screen.blit(set, textpos)
# 显示初始界面
pygame.draw.rect(screen, [0, 205, 0], [35, 210, 130, 20], 0)
Score('Play Game', 35, 210)
pygame.display.flip()
# 得分规则
Score_Rule = {
    1: 1,
    2: 3,
    3: 5,
    4: 8
}
# 存储用来查找判定哪一行是满行的的数据
block_blank = {i: [] for i in range(0, 400, 20)}
# 存储已下落固定的方块数据
block_one = []
# 一些初始判定值
y_min = 380     # 判断初始方块是否落到底部
decide = True   # 随机选择方块及初始化一些值得判定值
Play = False    # 游戏是否开始的判定值
score = '0'     # 玩家初始得分为0
# 主程序
while True:
    # 随机选择方块同时初始化一些值
    if decide:
        RGB = [34, 139, 34]     # 方块颜色
        col = 0                 # 方块一次下落的高度初始值
        row = 0                 # 旋转方块时的初始值
        num = random.randint(0, 6)      # 随机选择方块
        block = Block(80, 0)[num]
        a = block[0][0][0]      # 左移或右移的初始值
        decide = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 点击后开始游戏
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(35, 165) and event.pos[1] in range(210, 230):
            Play = True
            pygame.draw.rect(screen, [255, 255, 255], [0, 0, 200, 400], 0)
            pygame.draw.rect(screen, [250, 228, 181], [0, 400, 200, 440], 0)
            Score('Score:', 50, 410)
            Score(score, 130, 410)
        # 游戏结束后点击开始一局新游戏
        elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(35, 165) and event.pos[1] in range(280, 300):
            decide = True
            Play = True
            score = '0'
            pygame.draw.rect(screen, [255, 255, 255], [0, 0, 200, 440], 0)
            pygame.draw.rect(screen, [250, 228, 181], [0, 400, 200, 440], 0)
            Score('Score:', 50, 410)
            Score(score, 130, 410)
            pygame.display.flip()
            continue
        # 游戏结束后点击退出游戏
        elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(35, 165) and event.pos[1] in range(310, 330):
            sys.exit()
        # 旋转方块
        if event.type == pygame.KEYDOWN:
            # 判断方块是否可以旋转
            if event.key == pygame.K_UP:
                row += 1
                if row == len(block):
                    row = 0
                    if min([x[0] for x in block[row]]) < 0 or max([x[0] for x in block[row]]) > 180 or \
                            bool([z for z in [(x, y+col) for x, y in block[row]] if z in block_one]):
                        row = len(block)-1
                else:
                    if min([x[0] for x in block[row]]) < 0 or max([x[0] for x in block[row]]) > 180 or \
                            bool([z for z in [(x, y+col) for x, y in block[row]] if z in block_one]):
                        row -= 1
            # 点击左移方块
            elif event.key == pygame.K_LEFT and min([x[0] for x in block[row]]) > 0 and \
                    not bool([z for z in [(x-20, y+col) for x, y in block[row]] if z in block_one]):
                a -= 20
                block = Block(x=a, y=0)[num]
            # 点击右移方块
            elif event.key == pygame.K_RIGHT and max([x[0] for x in block[row]]) < 180 and \
                    not bool([z for z in [(x+20, y+col) for x, y in block[row]] if z in block_one]):
                a += 20
                block = Block(x=a, y=0)[num]
            # 点击使当前方块快速下落
            elif event.key == pygame.K_DOWN:
                if not bool(block_one):
                    col = 380
                else:
                    if col < min([i[1] for i in block_one])-20:
                        col = min([i[1] for i in block_one])-20
    # 判断游戏是否结束
    if bool(block_one):
        if min([x[1] for x in block_one]) <= 0:
            Play = False
            decide = False
            pygame.draw.rect(screen, [255, 255, 255], [0, 0, 200, 440], 0)
            Score('Game Over', 35, 100)
            Score('Your Score:', 20, 130)
            Score(score, 160, 130)
            pygame.draw.rect(screen, [0, 205, 0], [35, 280, 130, 20], 0)
            pygame.draw.rect(screen, [0, 205, 0], [35, 310, 130, 20], 0)
            Score('New Game', 35, 280)
            Score('Exit Game', 35, 310)
            pygame.display.flip()
            block_one = []
    # 游戏开始
    if Play:
        # 随机落下的方块在屏幕上逐步下落
        for i, j in block[row]:
            pygame.draw.rect(screen, RGB, [i, j+col, 20, 20], 0)
        ChessBoard()
        pygame.display.flip()
        for i, j in block[row]:
            pygame.draw.rect(screen, [255, 255, 255], [i, j+col, 20, 20], 0)
        # 方块下落时间间隔
        pygame.time.delay(500)
        # 判断是否有满行
        if col == 380 or bool([z for z in [(x, y+col+20) for x, y in block[row]] if z in block_one]):
            # 将随机下落的方块在固定后将其显示在屏幕上
            for i, j in block[row]:
                pygame.draw.rect(screen, RGB, [i, j+col, 20, 20], 0)
                block_one.append((i, j+col))
                if j+col > 0:
                    block_blank[j+col].append((i, j+col))
            new_row = []    # 用来记录满行的数量
            # 消除满行并将其从block_one中删除
            for i in sorted(block_blank.keys(), reverse=True):
                if len(block_blank[i]) == 10:
                    new_row.append(i)
                    pygame.draw.rect(screen, [255, 255, 255], [0, i, 200, 20], 0)
                    block_one = list(set(block_one) ^ set(block_blank[i]))
            # 消除满行后，将屏幕上剩余的方块根据消除的行数下移
            if bool(new_row):
                score = str(Score_Rule[len(new_row)] + int(score))
                pygame.draw.rect(screen, [255, 255, 255], [130, 410, 60, 20], 0)
                Score(score, 130, 410)
                block_blank = {i: [] for i in range(0, 400, 20)}
                for i in sorted(new_row):
                    for j in block_one:
                        if j[1] < i:
                            block_one[block_one.index(j)] = (j[0], j[1]+20)
                        pygame.draw.rect(screen, [255, 255, 255], [j[0], j[1], 20, 20], 0)
                for i in block_one:
                    block_blank[i[1]].append(i)
                    pygame.draw.rect(screen, [34, 139, 34], [i[0], i[1], 20, 20], 0)
            new_row = []    # 初始化
            ChessBoard()
            pygame.display.flip()
            col = 0         # 初始化
            decide = True
        col += 20
