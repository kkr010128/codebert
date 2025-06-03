import numpy

n, m = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
sup_A = 10 ** 5
B = [0] * (1 << 18)
for a in A:
    B[a] += 1
C = numpy.fft.fft(B)
D = numpy.fft.ifft(C * C)

ans = 0
cnt = 0
for i in range(2 * sup_A, -1, -1):
    d = int(D[i].real + 0.5)
    if cnt + d >= m:
        ans += (m - cnt) * i
        break
    cnt += d
    ans += i * d

print(ans)