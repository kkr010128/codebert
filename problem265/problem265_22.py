n = int(input())

dic = {}
for i in range(1,50000):
    dic[int(i * 1.08)] = i

if n in dic:
    print(dic[n])
else:
    print(':(')