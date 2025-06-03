A,B,K = map(int, input().split())

print(A-K, B) if K <= A else print(0,0) if (A+B) <= K else print(0, A+B-K)
