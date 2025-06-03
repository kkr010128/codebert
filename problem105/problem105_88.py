n = int(input())
lst = list(map(int, input().split()))
count = 0
for x in range(1,n+1,2):
    if lst[x-1]%2 != 0:
        count +=1
print(count)