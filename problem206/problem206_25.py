N=input()

N=int(N)

q1, mod = divmod(N,2)

if mod == 0:
    print(q1)
else:
    print(q1 + 1)