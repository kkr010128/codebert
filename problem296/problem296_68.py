S = input()
K = int(input())


if len(set(S)) == 1:
    print(len(S)*K//2)
else:
    i, count1 = 1, 0
    while i < len(S):
        if S[i] == S[i-1]:
            count1 += 1
            i += 2
        else:
            i += 1
    ss = S*2
    i, count2 = 1, 0
    while i < len(ss):
        if ss[i] == ss[i-1]:
            count2 += 1
            i += 2
        else:
            i += 1
    print(count1+(count2-count1)*(K-1))
