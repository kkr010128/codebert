N = int(input())
Numbers = list(map(int,input().split()))
temp_min = Numbers[0]
count = 0
for i in range(N):
    if Numbers[i] <= temp_min:
        temp_min = Numbers[i]
        count = count+1
print(count)