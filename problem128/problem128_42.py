x,n = map(int,input().split())
p = list(map(int,input().split()))
dic = {}
lis = []
for i in range(0,102):
    if i not in p:
        dic[i] = abs(x-i)
        lis.append(i)

mini = min(dic.values())
for j in lis:
    if mini == dic[j]:
        print(j)
        break