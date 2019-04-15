# https://pintia.cn/problem-sets/994805260223102976/problems/994805321640296448
# 正确
n = int(input())
maxstu_score = -1
minstu_score = 101
maxstu = ''
minstu = ''
while n>0:
    str_temp = input()
    list1 = str_temp.split(' ')
    score_temp = int(list1[2])
    if score_temp >= maxstu_score:
        maxstu_score =score_temp
        maxstu = str_temp
    if score_temp <= minstu_score:
        minstu_score = score_temp
        minstu = str_temp
    n = n - 1 
print(maxstu[0:maxstu.rfind(' ')])
print(minstu[0:minstu.rfind(' ')])
