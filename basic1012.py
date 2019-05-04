# https://pintia.cn/problem-sets/994805260223102976/problems/994805311146147840
# 正确
flag=1 # 
in1 = "8 1 2 4 5 6 7 9 16" if flag==0 else input()
n=in1.split()
n_num=[int(i) for i in n]
a1=0 # 求和
a1_count=0
a2=0 # 交错求和
a2_count=0
a3_count=0
a4_sum=0
a4_count=0
a5=-1
a5_count=0
for i in range(1,n_num[0]+1):
    tem=n_num[i]%5

    if tem==1: # a2交错求和

        a2=((-1)**a2_count)*n_num[i]+a2
        a2_count=a2_count+1
    elif tem==2: # a3 求个数
        a3_count=a3_count+1
    elif tem==3: # a4 求平均数
        a4_count=a4_count+1
        a4_sum=n_num[i]+a4_sum
    elif tem==4: # a5 求最大数
        a5_count=a5_count+1
        if n_num[i]>a5:
            a5=n_num[i]
    elif tem==0 and (n_num[i]%2 ==0):
        a1_count=a1_count+1
        a1=a1+n_num[i]
if a4_count==0:
    a4="N"
    pass
else:
    a4=a4_sum/a4_count
a3=a3_count
a1="N" if a1_count==0 else a1
a2="N" if a2_count==0 else a2
a3="N" if a3_count==0 else a3
# a4="N" if a4_count==0 else a4
a5="N" if a5_count==0 else a5

print(a1,a2,a3,sep=" ",end=" ")
if a4!="N":
    print("%.1f"%(a4),end=" ")
else:
    print(a4,end=" ")
print(a5,end="")
        

