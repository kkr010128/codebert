n = int(input())
rate = 1.08
for i in range(1,n+1):
    val = int(i*rate)
    if val == n:
        print(i)
        exit()
print(":(")