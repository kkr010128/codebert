n = int(input())
a = list(map(int, input().split()))

ans_list = [None for _ in range(n)]
for i in range(0, n):
    ans_list[a[i] - 1] = str(i + 1)
print(" ".join(ans_list))
