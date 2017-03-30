# -*-coding:utf8-*-
class Nation:
    def __init__(self, nation, gold, silver, curprum):
        self.nation = nation
        self.gold = gold
        self.silver = silver
        self.curprum = curprum

    def medal(self):
        totality = self.gold + self.silver + self.curprum
        print "%s %d %d %d %d" % (self.nation, self.gold, self.silver, self.curprum, totality)
        return totality

    def total_rank(self, total_num):
        return sorted(total_num, reverse=True, key=lambda x: x[4])

    def gold_rank(self, gold_num):
        return sorted(gold_num, reverse=True, key=lambda x: x[1])

    def result_print(self, result):
        for i in result:
            print """
%s 金：%d 银：%d 铜：%d 总：%d""" % (i[0], i[1], i[2], i[3], i[4]),

if __name__ == '__main__':
    all = [['美国', 46, 37, 38],['英国', 27, 23, 17],['中国', 26, 18, 26],['俄国', 19, 18, 19]]
    result = []
    for i in all:
        load_country = Nation(i[0], i[1], i[2], i[3])
        i.append(load_country.medal())
        result.append(i)
    print '\n按总奖牌数排名：',
    load_country.result_print(load_country.total_rank(result))
    print '\n\n按金牌数排名：',
    load_country.result_print(load_country.gold_rank(result))
