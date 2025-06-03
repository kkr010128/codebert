n = int(input())
count = 0
for i in range(n):
    a,b = map(int,input().split())
    if count >2 :
        break
    elif a==b:
        count += 1
    else:
        count = 0
print('Yes' if count > 2 else 'No')
