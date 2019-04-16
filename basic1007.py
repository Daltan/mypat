# https://pintia.cn/problem-sets/994805260223102976/problems/994805317546655744
# 正确
n = int(input())
if n <= 3:
    print(0)
else:
    l1 = [False if i % 2 ==0 else True for i in range(0,n+1) ] # 偶数是False
    i = 3
    j = 0
    while i <= int(n**0.5):
        if l1[i]: # 如果当前是素数
            j = i+i
            while j<n:
                l1[j] = False
                j = j+i
        i = i+2
    result =0
    for i in range(2,len(l1)-1):
        if l1[i] and i+2<len(l1):
            if l1[i+2]:
                result =result+1
    print(result)
