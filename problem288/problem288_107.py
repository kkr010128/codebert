N = int(input())

divisors = []

i = 1
while i*i <= N:
    if N % i == 0:
        divisors.append(i)
    i += 1

print(divisors[-1] + N // divisors[-1] - 2)