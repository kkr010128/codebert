N = list(input())

inN = [int(s) for s in N]

if sum(inN) % 9 == 0:
    print('Yes')
else:
    print('No')
