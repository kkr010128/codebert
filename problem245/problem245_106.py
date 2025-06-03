def resolve():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(len(S)-2):
        if S[i:i+3] == "ABC":
            cnt += 1
    print(cnt)

if '__main__' == __name__:
    resolve()