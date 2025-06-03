N = int(input())

a_array = []
b_array = []

for i in range(N):
    a, b = map(int, input().split())
    a_array.append(a)
    b_array.append(b)

a_array.sort()
b_array.sort()

if N % 2 != 0:
    mid_min = a_array[(N - 1) // 2]
    mid_max = b_array[(N - 1) // 2]
    print(mid_max - mid_min + 1)

else:
    mid_min = (a_array[N // 2 - 1] + a_array[N // 2]) / 2
    mid_max = (b_array[N // 2 - 1] + b_array[N // 2]) / 2
    print(int((mid_max - mid_min) * 2) + 1)
