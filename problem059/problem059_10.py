r, c = map(int, input().split())
hyou = []
tate_sum = [0] * (c + 1)
for i in range(r):
    line = list(map(int, input().split()))
    line.append(sum(line))
    tate_sum = [tate_sum[j] + line[j] for j in range(len(line))]
    hyou.append(" ".join(map(str, line)))
    
hyou.append(" ".join(map(str, tate_sum)))
print("\n".join(hyou))