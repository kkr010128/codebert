H = int(input())
W = int(input())
N = int(input())

A_div, A_mod = divmod(N, H)
if A_mod != 0:
    A_div += 1

B_div, B_mod = divmod(N, W)
if B_mod != 0:
    B_div += 1

print(min(A_div, B_div))