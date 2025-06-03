N, K, S = map(int, input().split())
print(" ".join([str(S)] * K + [str(S+1)] * (N-K)) if S<10**9 else " ".join([str(S)] * K + ['1'] * (N-K)))
