S = input()
count_more = 0
count_less = 0
ans = 0
pre_si = '>'
for i, si in enumerate(S):
    if pre_si == '>' and si == '<':
        max_n = max(count_more, count_less)
        min_n = min(count_more, count_less)
        ans += (max_n+1)*(max_n)//2
        # print(i, ans)
        ans += (min_n)*(min_n-1)//2
        count_more = 0
        count_less = 0
        # print(i, ans)
    if si == '<':
        count_more += 1
    elif si == '>':
        count_less += 1
    pre_si = si
max_n = max(count_more, count_less)
min_n = min(count_more, count_less)
ans += (max_n+1)*(max_n)//2
ans += (min_n)*(min_n-1)//2
print(ans)        
