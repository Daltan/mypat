# https://pintia.cn/problem-sets/994805260223102976/problems/994805318855278592
# 正确
def sub_func (a:tuple()):
    b=a[0]
    s=a[1]
    g=a[2]
    while b>0:
        print('B',sep='',end='')
        b = b - 1
    while s >0:
        print('S',sep='',end='')
        s=s-1
    for i in range(1,g+1):
        print(i,sep='',end='')

n = input()
length = len(n)
l1 = [0,0,0]
l2 = [int(i) for i in n]
for i in range(length-1,0-1,-1): # 这一步废了很多脑筋。。。
    l1[i-length]=l2[i]
sub_func(tuple(l1))
