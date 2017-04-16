# (A,Z)>(65,90) (a,z)>(97,122)
import random
lst = [i for i in range(65,91)]+[j for j in range(97,123)]
for k in range(2000):
    lst1 = lst[:]
    lst2 = []
    for s in range(8):
        m = random.choice(lst1)
        n = chr(m)
        lst2.append(n)
        lst1.remove(m)
    print ''.join(lst2)
    lst2 = []
