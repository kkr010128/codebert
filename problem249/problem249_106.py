A, B, K = map(int, input().split())
 
d = min(A, K)
#print('d:', d)
A -= d
K -= d
d = min(B, K)
#print('d:', d)
B -= d
K -= d
 
print(A, B)