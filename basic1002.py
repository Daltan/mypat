strn = input()
list1= ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
sum = 0
for i in strn:
    sum = int(i) + sum
result = []
for i in str(sum):
    result.append(list1[int(i)])
print(' '.join(result))