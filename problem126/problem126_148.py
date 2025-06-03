k = input().split()

num = len(k)

for i in range(num):
    if k[i] == "0":
        print(i+1)