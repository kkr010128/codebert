n = int(input())

count = 0

if n%2==0:
    for i in range(int(n/2)-1):
        count += int((n-1)/(i+1))
    count += int(n/2)

else:
    for i in range(int(n/2)):
        count += int((n-1)/(i+1))
    count += int(n/2)

print(count)
