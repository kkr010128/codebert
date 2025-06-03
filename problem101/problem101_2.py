# M-SOLUTIONS プロコンオープン 2020: B – Magic 2
A, B, C = [int(i) for i in input().split()]
K = int(input())

is_success = 'No'

for i in range(K + 1):
    for j in range(K + 1):
        for k in range(K + 1):
            if i + j + k <= K and A * 2 ** i < B * 2 ** j < C * 2 ** k:
                is_success = 'Yes'

print(is_success)