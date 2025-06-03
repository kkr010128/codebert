X = int(input())
prime_under_X = []
for i in range(2, int(X ** 0.5) + 1):
    flg = True
    for j in range(len(prime_under_X)):
        if i % prime_under_X[j] == 0:
            flg = False
            break
    if flg:
        prime_under_X.append(i)

while True:
    flg = True
    for j in range(len(prime_under_X)):
        if X % prime_under_X[j] == 0:
            flg = False
            break
    if flg:
        print(X)
        break
    X = X + 1
