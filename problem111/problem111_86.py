n = int(input())
a = list(map(int, input().split()))
print(sum(sorted(a * 2)[::-1][1:n]))