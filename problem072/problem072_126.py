n = int(input())
data = [input().split() for i in range(n)]
for i in range(n - 2):
    if int(data[i][0]) == int(data[i][1]) and int(data[i + 1][0]) == int(data[i+1][1]) and int(data[i+2][0]) == int(data[i+2][1]):
        print('Yes')
        break
else:
    print('No')