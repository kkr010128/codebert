def resolve():
    S = list(input())
    T = list(input())
    cnt = 0
    for i in range(len(S)):
       if S[i] != T[i]:
            cnt += 1
    print(cnt)

if '__main__' == __name__:
    resolve() 