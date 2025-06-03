# coding: utf-8
# Your code here!

S = input()
T = input()

ans = 10000000
for i in range(len(T), len(S)+1):
    sub_S = S[i-len(T):i]
    
    count = 0
    for j in range(len(sub_S)):
        if T[j] != sub_S[j]:
            count += 1
    ans = min(ans, count)

print(ans)