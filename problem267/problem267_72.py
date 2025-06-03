import collections
N = int(input())
S = input()
S_list = [S[i] for i in range(N)]
S_c = collections.Counter(S_list)
list12 = []
list1 = []

ans = 0
for i in range(N-2):
    s1 = S_list[i]

    S_c[s1] = S_c[s1]-1
    if s1 in list1:
        continue

    S_c23 = S_c.copy()
    list1.append(s1)
    for j in range(i+1,N-1):
        s2 = S_list[j]
        
        S_c23[s2] = S_c23[s2] - 1
        if (s1+s2) in list12:
            continue
        else:
            list12.append(s1+s2)
            for key in S_c23.keys():
                if S_c23[key] != 0:
                    ans+=1
print(ans)