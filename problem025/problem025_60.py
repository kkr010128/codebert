def calc(s, i):
    global n
    global anslst
    global nlst
    if i == n:
        anslst[s] = 'yes'
        return

    calc(s, i+1)
    calc(s + nlst[i], i+1)


anslst = ['no']*2001
n = int(input())
nlst = list(map(int, input().split()))
q = int(input())
qlst = list(map(int, input().split()))

calc(0, 0)

for i in qlst:
    print(anslst[i])
