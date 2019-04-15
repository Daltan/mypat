# https://pintia.cn/problem-sets/994805260223102976/problems/994805320306507776
# 正确（最后四行输出代码，占用了我40%的时间。。。）
n = input()
str_origin = input()
list_origin = str_origin.split(' ')
s1 = set(list_origin)
# print("初始s1:",s1)
for i in list_origin:
    i = int(i)
    # print('当前',i)
    while (i != 1):
        if (i%2==0):
            i = i // 2
        else:
            i = (i*3 +1)//2
        # print('current i = ', i)
        if (str(i) in s1):
            # print('remove',str(i))
            s1.remove(str(i))
result= [int(i) for i in s1]
result.sort(reverse = True)
result_int = [str(i) for i in result]
print(" ".join(result_int))
