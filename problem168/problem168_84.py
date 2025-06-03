# B - Homework

# N M
N, M = map(int, input().split())
my_list = list(map(int, input().split(maxsplit=M)))

if N < sum(my_list):
    answer = -1
else:
    answer = N - sum(my_list)

print(answer)
