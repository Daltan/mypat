# https://pintia.cn/problem-sets/994805260223102976/problems/994805325918486528
# 正确
n = int(input())
step = 0
while n != 1:
    if(n % 2 ==0):
        n = n/2
        step = step + 1
    else:
        n = (3 * n + 1) / 2
        step = step + 1
print(step)
