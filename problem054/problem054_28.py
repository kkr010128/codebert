ans = [f'{x} {y + 1}' for x in "SHCD" for y in range(13)]

n = int(input())
for i in range(n):
    a = input()
    ans.remove(a)

for v in ans:
    print(v)
