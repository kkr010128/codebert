k=int(input())
count=1
num=7
for _ in range(k):
    if num%k == 0:
        print(count)
        break
    else:
        count += 1
        num = (num % k)*10 + 7
else:
    print(-1)