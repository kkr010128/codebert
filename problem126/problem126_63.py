n = list(input().split())

for i in range(len(n)):
    if n[i] == "0":
        print(int(i)+1)
