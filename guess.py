# -*-coding:utf8-*-
import random               # 调用随机模块


def compare(ans, num):      # 定义比较大小的函数
    if ans < num:
        print '太小了！'
        return False
    elif ans > num:
        print '太大了！'
        return False
    else:
        print '猜对了！'
        return True


def guess(lst):             # 定义用来统计玩家战绩的函数
    total_degree = lst[0]   # 总次数
    correct_times = lst[1]  # 猜对次数
    total_round = lst[2]    # 总轮数
    # average_win = lst[3]
    decide = True
    while decide:
        play = raw_input('1.开始游戏，2.退出游戏:\n')
        total_round += 1    # 游戏开始，总轮数加1
        if play == '1':
            num = random.randint(0, 100)    # 获取被猜的100以内的随机整数
            round_times = 0                 # 每一轮猜数字前，初始化每轮已猜次数
            judge = False
            while not judge:
                if round_times < 6:         # 每一轮猜数字只有6次机会，即便猜不对，6次后会提示重新开始新一轮
                    ans = raw_input('猜一个100以内的整数：\n')
                    if ans.isdigit() and int(ans) in range(0, 100):   # 将玩家输入的一切非整数字符及不在100以内的字符过滤掉
                        round_times += 1
                        total_degree += 1
                        judge = compare(int(ans), num)  # 条用比大小函数
                        if judge:           # 判断是否猜对
                            correct_times += 1
                    else:
                        print '你应该猜一个100以内的整数的,重新开始游戏吧'
                        break
                else:
                    print "本轮机会用完也没猜对，再开一轮吧！"
                    break
            if correct_times:   # 避免因猜对次数为零时的除零错误
                average_win = '%.1f' % (total_degree / float(correct_times))
            else:
                average_win = 0
            lst[0] = total_degree
            lst[1] = correct_times
            lst[2] = total_round
            lst[3] = average_win
            players[game_player] = lst  # 将本轮游戏战绩记录并保存
        elif play == '2':
            decide = False
        else:
            print "请按提示输入，到底是开始游戏，还是退出游戏，好吗？"
    return players
try:
    with open('players.txt') as g:  # 打开并读取玩家资料
        old_players = g.readlines()
        players = {}                # 初始化一个用来保存临时玩家信息的字典
        for i in old_players:       # 依次读取老玩家战绩，并存储到players字典中
            name = ((i.strip()).split(' '))[0]
            score = ((i.strip()).split(' '))[1:]
            combat_gains = []
            for j in score:
                if score.index(j) < (len(score)-1):
                    combat_gains.append(int(j))
                else:
                    combat_gains.append(float('%.2f' % (float(score[-1]))))
            players[name] = combat_gains
    game_player = raw_input('请输入用户名:\n')
    if game_player in players.keys():       # 判断玩家是新玩家还是老玩家
        print "%s 欢迎回来，祝你游戏愉快！" % game_player   # 若是老玩家则输出其之前战绩
        print "战绩：共猜过%d次、猜对%d次、共猜了%d轮、平均%.2f次猜对一次。" % (
            players[game_player][0], players[game_player][1], players[game_player][2], players[game_player][3])
        combat_gains = players[game_player]
        guess(combat_gains)                 # 调用统计玩家战绩函数
    else:                                   # 若为新玩家，则将其战绩初始化并保存
        print "欢迎%s来到猜数字游戏，祝你游戏愉快！" % game_player
        print "目前你还没有战绩"
        combat_gains = [0, 0, 0, 0]
        guess(combat_gains)                 # 调用统计玩家战绩函数
    with open('players.txt', 'w') as f:     # 将战绩保存至本地文件
        for i in players.keys():
            player_name = i
            for j in players[i]:
                player_name = player_name + ' ' + str(j)
            f.write(player_name + '\n')
except:
    print '游戏错误'
finally:
    print '游戏结束！'
