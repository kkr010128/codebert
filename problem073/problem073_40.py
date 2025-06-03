def make_divisors(n):
    cnt = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
        i += 1
    return cnt
numbers = [1,10, 100, 1000, 10000, 100000, 150000,200000, 250000,300000,350000, 400000,450000, 500000,550000,600000,630000,675000,700000,720000,750000,800000,825000,850000,875000,900000,912500,925000,950000,975000,987500,1000000]
datas = [0,23,473,7053,93643,1166714, 1810893, 2472071, 3145923, 3829761, 4522005,5221424,5927120,6638407,7354651,8075420,8509899,9164377,9529244,9821778,10261678,10997400,11366472,11736253,12106789,12478098,12664043,12850013,13222660,13595947,13782871,13969985]

N = int(input())
ttl = 0
numPin = 0

for i in range(len(numbers)):
    if N == 1000000:
        numPin = len(numbers) - 1
        break
    if numbers[i] <= N < numbers[i+1]:
        numPin = i
        break

if numPin != len(numbers)-1:
    if N - numbers[numPin] < numbers[numPin + 1] - N:
        for i in range(numbers[numPin], N):
            ttl += make_divisors(i)
        print(ttl + datas[numPin])
    else:
        for i in range(N,numbers[numPin+1]):
            ttl -= make_divisors(i)
        print(ttl + datas[numPin + 1])
else:
    print(datas[numPin])
