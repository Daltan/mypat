# 临时文件 用于实验
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
            # print('当前j',j,sep=':')

            while j<n:
                l1[j] = False
                j = j+i
                # print('当前j',j,sep=':')
        # print('i: ',i)
        i = i+2
    # for i in range(3,int(n**0.5)):
    # for i in range(2,len(l1)):
    #     if l1[i] :
    #         print (i, end=',')
    # que = [0,0]
    result =0
    for i in range(2,len(l1)-1):
        if l1[i] and i+2<len(l1):
            if l1[i+2]:
                # print('第{}对：{},{}'.format(result+1, i,i+2))
                result =result+1
    print(result)
