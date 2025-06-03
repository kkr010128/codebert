from numpy import cumsum

N = int(input())
A = list(map(int, input().split()))
a_cum = cumsum(A)
cand = [abs(a_cum[i] - (a_cum[-1] - a_cum[i])) for i in range(N)]
print(min(cand))
