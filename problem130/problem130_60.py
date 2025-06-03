S = input()
ans = []
for i in range(len(S)+1):
    if i <= 2 :
        ans += S[i]
    else:
        print(''.join(ans))
        exit()
