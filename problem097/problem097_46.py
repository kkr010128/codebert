K = int(input())

if K % 2 == 0 or K % 5 == 0:
    print(-1)
    exit()

i = 0
ai = 0
while True:
    ai = (ai * 10 + 7) % K
    i += 1
    if ai == 0:
        break
print(i)