# -*- coding: utf8 -*-
score_gpa = [
    [90, 100, 4],
    [85, 90, 3.7],
    [82, 84, 3.3],
    [78, 81, 3],
    [75, 77, 2.7],
    [71, 74, 2.3],
    [66, 70, 2],
    [62, 65, 1.7],
    [60, 61, 1.3],
    [0, 60, 0]
]
score_gpa_lst = []
while True:
    score = raw_input("Please input your score:")
    if score.isdigit() and int(score) in range(0, 101):
        for i in score_gpa:
            if int(score) in range(i[0], i[1]+1):
                score_gpa_lst.append([int(score), i[2]])
    elif not bool(score):
        score_gpa = sum([x[0] * x[1] for x in score_gpa_lst]) / sum([x[0] for x in score_gpa_lst])
        print "Your Score GPA:%.2f" % score_gpa
        break
    else:
        print "Input Error"
