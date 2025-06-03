N = int(input())
li = list(map(int,input().rstrip().split(' ')))
count = 0
for i in li[0::2]:
    if i%2==1:count += 1
print(count)