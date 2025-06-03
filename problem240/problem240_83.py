import sys

def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]


def main():
    N, M = MI()

    p = ["0"]*(M)
    S = ["0"]*(M)
    for i in range(M):
        p[i], S[i] = map(str,input().split())

    ans = [0]*(N+1)
    error = [0]*(N+1)
    e = [0]*(N+1)

    for i in range(M):
        if ans[int(p[i])] == 0:
            if S[i] == "WA":
                error[int(p[i])] += 1
            elif S[i] == "AC":
                ans[int(p[i])] = 1

    sum_ans = sum(ans)
    sum_error = 0
    for i in range(N+1):
        if ans[i] == 1:
            sum_error += error[i]
    print(sum_ans, sum_error)

if __name__ == "__main__":
	main()