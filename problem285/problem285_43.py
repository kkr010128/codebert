
s = input()
data = []
cnt = 0
for i in range(len(s)-1):
    cnt += 1
    if s[i] != s[i+1]:
        if s[i] == "<" and s[i+1] == ">":
            data.append(cnt)
            data.append(-1)
        else:
            data.append(cnt)
        cnt = 0
data.append(cnt+1)

for i in range(len(data)-1):
    if data[i] == -1:
        if data[i-1] < data[i+1]:
            data[i-1] -= 1
        else:
            data[i-1] > data[i+1]
            data[i+1] -= 1

ans = 0
for i in range(len(data)):
    if data[i] != -1:
        for j in range(1, data[i]+1):
            ans += j

# print(data)
print(ans)
