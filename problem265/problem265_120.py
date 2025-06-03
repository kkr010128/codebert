import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()
for i in range(50000):
    if i*27//25 == N:
        print(i)
        break
else:
    print(':(')
