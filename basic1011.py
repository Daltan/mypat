#https://pintia.cn/problem-sets/994805260223102976/problems/994805312417021952
# 正确
flag=1 # 
in1 = "1" if flag==0 else input()
n = int(in1)
n_final=n
while n > 0:
    in2 = "1 2 3" if flag==0 else input()
    tem_str=in2.split()
    num=[int(i) for i in tem_str]
    tag=str(n_final-n+1)
    if num[0]+num[1]>num[2]:
        print("Case #"+tag+": true")
    else:
        print("Case #"+tag+": false")
    n = n-1