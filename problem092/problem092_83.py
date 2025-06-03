# string
# a, b, c = input().split()
# str_list = list(input().split())

# number
# a, b, c = map(int, input().split())
# num_list = list(map(int, input().split()))

# lows
# str_list = [input() for _ in range(n)]

# many inputs
# num_list = []
# for i in range(n): num_list.append(list(map(int, input().split())))

x, k, d = map(int, input().split())

if x < 0:
    x = -x

l = int(x/d)

if l < k:
    print(abs(x - ((k-l)%2 + l) * d))
else:
    print(abs(x - k*d))