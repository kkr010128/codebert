N = int(input())

count = 0
for i in range(N):
    count += int((N-1)/(i+1))
print(count)
