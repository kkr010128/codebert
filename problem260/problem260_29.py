# ABC149
# A Blackjack
A = list(map(int, input().split()))
a = sum(A)
if a > 21:
    print("bust")
else:
    print("win")
