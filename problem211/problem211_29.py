#K = input()
NR = list(map(int, input().split()))
#s = input().split()
#N = int(input())

if (NR[0] >= 10):
    print(NR[1])
else:
    print(NR[1] + 100 * (10 - NR[0]))