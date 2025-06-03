n = int(input())
for x in range(1, 50005):
    if x * 108//100 == n:
        print(x)
        exit()
else:
    print(':(')