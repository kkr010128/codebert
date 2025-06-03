n = int(input())
count=0

for i in range(1,n//2+1):
    j = n - i
    if i != j:
        count += 1

print(count)