N = int(input())

for i in range(10):
    for j in range(10):
        if i * j == N:
            print("Yes")
            exit(0)
else:
    print("No") 