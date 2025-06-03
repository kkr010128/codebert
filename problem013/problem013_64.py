n = int(input())
ls = [int(input()) for _ in range(n)]

result = []
biggest = 0
for i in range(n-1):
    last = ls.pop()
    if last > biggest:
        biggest = last
        result.append(last - min(ls))
print(max(result))
