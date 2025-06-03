n = int(input())
cnt = 0

for i in range(1, 10):
    if len(str(n//i)) == 1 and n%i == 0:
        cnt +=1

if cnt >= 1:
    print('Yes')
else :
    print('No')
