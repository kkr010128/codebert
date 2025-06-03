N = int(input())
moji = str(input())

if len(moji) <= N:
    print(moji)
else:
    print(moji[:N] + "...")