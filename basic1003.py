n = input()
while n>0:
    str1 = input()
    if(judge(str1)==True):
        print('YES')
    else:
        print('NO')
    n = n -1
def judge(str1):
    if 'P' in str1:
        inx = str1.find('P')
        
    return False