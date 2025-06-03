n=int(input())
for i in range(1,50001):
    if i*108//100 == n:
        print(i)
        break
else:
    print(":(")