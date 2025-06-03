N, R = map(int, input().split())
 
# min()でまとめて書ける
print(R + 100 * (10-min(10, N)))