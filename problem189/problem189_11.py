import math
N, M = list(map(int, input().split()))
n_pairs = math.factorial(N) // (2*math.factorial(N-2)) if N > 1 else 0
m_pairs = math.factorial(M) // (2*math.factorial(M-2)) if M > 1 else 0
print(n_pairs + m_pairs)