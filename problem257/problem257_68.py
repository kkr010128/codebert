n = input()
renga = list(map(int, input().split(" ")))

ni = 1
remains = 0

for r in renga:
    if ni == r:
        ni += 1
        remains += 1
if ni == 1:
    print(-1)
else:
    print(len(renga) - remains)
