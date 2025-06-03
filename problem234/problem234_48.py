def MAP(): return map(int, input().split())
def LIST(): return list(MAP())
 
N = int(input())
count = [[0 for _ in range(10)] for _ in range(10)]
for i in range(1, N + 1):
    string_i = str(i)
    initial = int(string_i[0])
    end = int(string_i[-1])
    count[initial][end] += 1
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += count[i][j] * count[j][i]
print(ans)