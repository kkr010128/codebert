N = int(input())
x = int(N/1.08)
for i in range(x, x+2):
    if N == int(i*1.08):
        print(i)
        break
else:
    print(":(")