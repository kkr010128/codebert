N = int(input())
S = list(map(int,input().split()))
B= list()
X = list()
for i in S:
    if i % 2== 0:
        B.append(i)
for n in B:
    if n % 3 == 0 or n % 5 == 0:
        X.append(n)
if len(B) == len(X):
    print('APPROVED')
else:
    print('DENIED')


