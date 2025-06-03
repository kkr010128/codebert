N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_A = [0] * (N + 1)
sum_B = [0] * (M + 1)

for a in range(1, N + 1):
    sum_A[a] = sum_A[a - 1] + A[a - 1]
for b in range(1, M + 1):
    sum_B[b] = sum_B[b - 1] + B[b - 1]

count = 0

# print(sum_A)
# print(sum_B)
last_index = M

for a in range(len(sum_A)):
    # print("----------------------")
    # print("a", a)
    if sum_A[a] > K:
        count = max(count, a - 1)
        break
    elif sum_A[a] == K:
        count = max(count, a)
    now = sum_A[a]
    rest = K - now
    # print("last_index", last_index)
    #able = len([i for i in sum_B[:last_index + 1] if i <= rest]) - 1

    while True:
        if last_index < 0:
            able = 0
            break
        if sum_B[last_index] > rest:
            last_index -= 1
        else:
            able = last_index
            break

    # print("now", now, "rest", rest, "able", able)
    # print("今回の最大countは", "a + able = ", a + able)
    count = max(count, a + able)
    # print("これまでの最大count", count)

print(count)
