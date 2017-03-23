#coding:utf8
import random #调用随机模块
#定义比较大小的函数
def compare(ans,num):
    if ans<num:
        print '太小了！'
        return False
    elif ans>num:
        print '太大了！'
        return False
    else:
        print '猜对了！'
        return True
#定义用来判断你战绩的函数
def guess(lst):
    total_degree = lst[0]
    correct_times = lst[1]
    total_round= lst[2]
    average_win= lst[3]
    decide = True
    while decide:
        play = raw_input('1.开始游戏，2.退出游戏:\n')
        total_round += 1
        if play == '1':
            num = random.randint(0, 100)
            absolute_round = 0
            judge = False
            while not judge:
                if absolute_round < 6: #每轮只有6次机会
                    ans = raw_input('猜一个100以内的整数：\n')
                    if ans.isdigit():
                        absolute_round += 1
                        total_degree += 1
                        judge = compare(int(ans), num)
                        if judge:
                            correct_times += 1
                    else:
                        print '你应该猜一个整数的,重新开始游戏吧'
                        print "实在不想玩，也可以退出游戏"
                        break
                else:
                    print "本轮机会用完也没猜对，再开一轮吧！"
                    break
            if correct_times:
                average_win = '%.1f' % (total_degree / float(correct_times))
            else:
                average_win = 0
            lst[0] = total_degree
            lst[1] = correct_times
            lst[2] = total_round
            lst[3] = average_win
            players[game_player] = lst
        elif play == '2':
            decide = False
        else:
            print "请按提示输入，到底是开始游戏，还是退出游戏，好吗？"
    return players
#主程序运行，包含读取用户战绩，更新用户战绩
try:
    with open('players.txt','w') as new:
        pass
    with open('players.txt') as g:
        old_players=g.readlines()
        players={}
        for k in old_players:
            s1=((k.strip()).split(' '))[0]
            s2=((k.strip()).split(' '))[1:]
            combat_gains=[]
            for l in s2:
                if s2.index(l)<(len(s2)-1):
                    combat_gains.append(int(l))
                else:
                    combat_gains.append(float('%.2f'%(float(s2[-1]))))
            players[s1]=combat_gains
    game_player = raw_input('请输入用户名:\n')
    if game_player in players.keys():
        print "%s 欢迎回来，祝你游戏愉快！" % game_player
        print "战绩：共猜过%d次、猜对%d次、共猜了%d轮、平均%.2f次猜对一次。"%(
            players[game_player][0],players[game_player][1],players[game_player][2],players[game_player][3])
        combat_gains=players[game_player]
        guess(combat_gains)
    else:
        print "欢迎%s来到猜数字游戏，祝你游戏愉快！" % game_player
        print "目前你还没有战绩"
        combat_gains=[0,0,0,0]
        guess(combat_gains)
    with open('players.txt','w') as f:
        for i in players.keys():
            player_name=i
            for j in players[i]:
                player_name=player_name+' '+str(j)
            f.write(player_name+'\n')
except :
    print '游戏错误'
finally:
    print '游戏结束！'
