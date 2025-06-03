N = int(input())
a_lst = list(map(int, input().split()))

print(sum((i + 1) % 2 == 1 and a % 2 == 1 for i, a in enumerate(a_lst)))
