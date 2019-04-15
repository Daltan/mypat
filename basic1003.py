# https://pintia.cn/problem-sets/994805260223102976/problems/994805323154440192
# 结果是4/5正确。一个错误。
def judge2(str1:str):
    # print('进入judge 2 了')

    str_sub1 = str1.split('P')
    stra=str_sub1[0]
    str_sub2 = str_sub1[1].split('T')
    strb, strc=str_sub2[0],str_sub2[1]
    # print(stra,strb,strc,sep='|')
    if len(stra)*len(strb) == len(strc):
        return True
    else:
        return False
        
def judge(str1):
    import re
    teststr = str1
    pattern1 =re.compile(r'[^P^A^T]')
    match1 = pattern1.search(teststr)
    pattern2 = re.compile(r'[A]*PAT[A]*')
    match2 = pattern2.search(teststr)
    pattern3 = re.compile(r'[A]*P[A]+T[A]*')
    match3 = pattern3.search(teststr)
    if match1:
        return False
    elif match2:
        return True
    elif match3 :
        if judge2(str1):
            return True
        else:
            return False
    else:
        return  False
n = int(input())
while n>0:
    str1 = input()
    if(judge(str1)==True):
        print('YES')
    else:
        print('NO')
    n = n -1