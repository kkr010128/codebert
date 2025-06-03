import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
for i in range(int(N**.5),0,-1):
    if N % i == 0:
        print(i+(N//i)-2)
        exit()
