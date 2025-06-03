N = int(input())

n = str(N)

le = len(n)

M = 0

for i in range(le):
    nn = int(n[i])
    M += nn

if M % 9 == 0:
    print("Yes")
else:
    print("No")