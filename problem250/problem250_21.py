X = int(input())
lsx = [1]*(2*10**5)

for i in range(2,2*10**5):
    if lsx[i] == 1:
        for j in range(i,2*10**5//i):
            lsx[j*i] = 0

for i in range(X,2*10**5):
    if lsx[i] == 1:
        print(i)
        break