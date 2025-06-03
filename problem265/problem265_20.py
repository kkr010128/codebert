N = int(input())

X = int(N/1.08)

for i in [-1, 0, 1]:
    X_ = int((X+i)*1.08)
    if(X_ == N):
        print(X+i)
        exit()

print(':(')