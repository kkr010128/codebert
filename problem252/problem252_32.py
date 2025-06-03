N, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

# N, M = map(int, input().split())
# A = list(map(int, input().split()))

# print(len(A))

max_p = max(A)

X = max_p



cnt = [0 for x in range(100001)]
hpp = [0 for x in range(100001)]


# print(A)

for i in A:
    # print(i)
    # if cnt[i] != 0:
    #     continue
    cnt[i] += 1
    hpp[i] += i
# print(cnt[:100])

for i in range(1, 100001)[::-1]:
    cnt[i - 1] += cnt[i]
    hpp[i - 1] += hpp[i]

def countpair(left, x):
    # return cnt[x - left + 1] if (x - left > 0) else N
    if x - left <= 0:
        return N
    elif x - left > 100000:
        return 0
    else:
        return cnt[x - left]

def get_hpp(left, x):
    if x - left <= 0:
        return hpp[0]
    elif x - left > 100000:
        return 0
    else:
        return hpp[x - left]
# print(hpp[:100])


# print(cnt[:100])

small = 0
large = max_p * 2
threshold = 0
# d_c = 0

# mems = []

while (small <= large):
    # d_c += 1
    # print(small, large)
    X = (small + large) // 2

    nums = 0
    for i in range(N):
        left = A[i]
        # print(len(A))
        nums += countpair(left, X)

    if nums >= M:
        threshold = X
        small = X + 1
    else:
        large = X - 1

X = threshold

# print("X:", X)
# print("threshold:", threshold)

Y = X + 1

hpp_sum = 0
num_sum = 0

for i in range(N):
    # print("-----------")
    left = A[i]
    cnt_num = countpair(left, Y)
    num_sum += cnt_num
    # print("left:", left)
    # print("cnt_num:", cnt_num)
    hpp_sum += left * cnt_num
    # print("get_hpp:", get_hpp(left, Y))
    hpp_sum += get_hpp(left, Y)
    # print("hpp_sum:", hpp_sum)


hpp_sum += X * (M - num_sum) if (M - num_sum > 0) else 0

print(hpp_sum)


# print(out)

# for i in range(N):
