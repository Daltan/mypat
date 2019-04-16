# https://pintia.cn/problem-sets/994805260223102976/problems/994805316250615808
# 4/5 个正确，一个错误
nm = input()
m = int(nm.split(' ')[1])
l1_str = input()
l1 = [i for i in l1_str.split(' ')]
n = len(l1)
if n != 1:
    m_true = m % n
    l2=[]
    l2.extend( l1[n-m_true:])
    l2.extend(l1[:n-m])
    l3 = [str(int(i)) for i in l2]
    print(' '.join(l3))
else:
    print(int(l1_str))
