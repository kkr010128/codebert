N = int(input())

X = N / 1.08

X_down = int(X)
X_up = int(X) + 1

bool_down = int(X_down * 1.08) == N
bool_up = int(X_up * 1.08) == N

if bool_down:
    print(X_down)
elif bool_up:
    print(X_up)
else:
    print(":(")
