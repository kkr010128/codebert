N, S = int(input()), input()
print("Yes" if N%2 == 0 and S[:(N//2)] == S[(N//2):] else "No")