N = int(input())
A = []
for i in range(N+1):
    if i % 15 == 0:
        pass
    elif i % 3 == 0:
        pass
    elif i % 5 == 0:
        pass
    else:
        A.append(i)
print(sum(A))