N = int(input())

senter = N // 1.08

for i in range(1000):
    if int((senter-100+i) * 1.08) == N:
        print(int(senter-100+i))
        break
else:
    print(":(")
