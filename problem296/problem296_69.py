def solve(S):
    pre = S[0]
    flag = False
    ans = 0
    cnt = 0
    for s in S[1:]:
        if flag:
            if pre == s:
                cnt += 1
            else:
                ans += cnt // 2
                cnt = 0
                flag = False
        else:
            if pre == s:
                cnt += 2
                flag = True
        pre = s
    if flag:
        ans += cnt // 2
    return ans


S = input()
K = int(input())
if len(S) == 1:
    print(K // 2)
elif len(S) == S.count(S[0]):
    print((len(S)*K)//2)
else:
    if K == 1:
        print(solve(S))
    elif K == 2:
        print(solve(S + S))
    else:
        ans2 = solve(S + S)
        ans3 = solve(S + S + S)
        print(ans2 + (ans3-ans2)*(K - 2))
