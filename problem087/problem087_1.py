N = input()
USA = 0
n = 0
h = 0
k = 0
for i in range(0,len(N)):
    n += int(N[i])
if n % 9 == 0:
    print("Yes")
else:
    print("No")
    # h += 1
    # n += h
    # # if n == N+1:
    #     if n % 9 == 0:
