n,k,c = map(int,input().split())
S = input()
mae = []
ushiro = []
cur_1 = 0
temp_1 = 0
cur_2 = 0
temp_2 = 0
ans = []
for i in range(n):
    if S[i] == 'o' and temp_1 == 0:
        mae.append(i)
        cur_1 += 1
        temp_1 = c
    else:
        temp_1 = max(temp_1-1,0)
    if cur_1 == k:
        break
for i in range(n):
    if S[n-i-1] == 'o' and temp_2 == 0:
        ushiro.append(n-i-1)
        cur_2 += 1
        temp_2 = c
    else:
        temp_2 = max(temp_2-1,0)
    if cur_2 == k:
        break
for i in range(k):
    if mae[len(mae)-1-i] == ushiro[i]:
        ans.append(ushiro[i]+1)
if len(ans) == 0:
    None
else:
    ans.reverse()
    for i in range(len(ans)):
        print(ans[i])
