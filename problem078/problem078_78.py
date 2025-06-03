N = int(input())

def cal(N):
    return abs(10**N - 9**N - 9**N +  8**N) % (10**9+7)

print(cal(N))