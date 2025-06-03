K = int(input())

mod = 7
number = 1

for i in range(K):
    if mod % K == 0:
        break
    number += 1
    mod = (mod * 10 + 7) % K

if mod % K == 0:
    print(number)
else:
    print(-1)