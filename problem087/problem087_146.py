N = input()

Sum = 0
for n in list(N):
    Sum = Sum + int(n)

ANS = 'Yes' if Sum % 9 == 0 else 'No'
print(ANS)