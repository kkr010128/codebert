N = int(input())

az = [chr(i) for i in range(97, 97+26)]

N = N - 1

tmp1 = 0
for i in range(1, 1000):
    tmp1 += 26 ** i
    if tmp1 > N:
        num = i
        tmp1 -= 26 ** i
        N -= tmp1
        break

tmp = [0 for _ in range(num)]
for i in range(num):
    tmp[i] = N%26
    N = N // 26

ans = ""
for i in range(len(tmp)):
    ans = az[tmp[i]] + ans

print(ans)