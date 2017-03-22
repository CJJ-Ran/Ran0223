#coding:utf-8
original_scores=[]#用来存储原始成绩
average_scores=[]#用来存储含总分、平均分的成绩
rank_scores=[]#用来存储含名次的成绩
#读取原始成绩至original_sxores
with open('report.txt') as f:
    g=f.readlines()
    for i in g:
        original_scores.append(i.strip())
#计算每名同学的总分及平均分并保存
for j in original_scores:
    lst1=j.split(' ')
    sum=0
    aver=0
    for k in lst1[1:]:
        sum+=int(k)
    aver=sum/float(len(lst1[1:]))
    lst1.append(str(sum))
    lst1.append(str(aver)[:4])
    average_scores.append(lst1)
rank_scores=sorted(average_scores,key=lambda x:float(x[-1]),reverse=True)
#计算每科目平均成绩并保存
average=['平均',0,0,0,0,0,0,0,0,0,0,0]
for k in rank_scores:
    for t in range(1,12):
        if t<11:
            average[t]+=int(k[t])
        else:
            average[t]+=float(k[t])
m=0
for l in average[1:]:
    m+=1
    average[m]=str(float(l)/len(rank_scores))[:5]
rank_scores.insert(0,average)
#添加名次，并将每科目添加至首行
for n in range(len(rank_scores)):
    rank_scores[n].insert(0,str(n))
subjects=['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
rank_scores.insert(0,subjects)
#将60分以下成绩替换为不及格
for fail in rank_scores[2:]:
    for z in range(2,13):
        if z<12:
            if int(fail[z])<60:
                fail[z]='不及格'
        else:
            if float(fail[z])<60:
                fail[z]='不及格'
#将统计分析结果保存至新文件reports.txt中
with open('reports.txt','w') as o:
    for p in rank_scores:
        q='\t'.join(p)
        o.write(q+'\n')
