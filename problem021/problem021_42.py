lst = list(input())
v_lakes = []
idx_stack = []
for i, c in enumerate(lst):
    if (c == '\\'):
        idx_stack.append(i)
    elif (idx_stack and c == '/'):
        # 対応する'\\'の位置
        j = idx_stack.pop()
        v = i - j
        while (v_lakes and v_lakes[-1][0] > j):
            v += v_lakes.pop()[1]
        v_lakes.append((j, v))
ans = [len(v_lakes)]
v = [v[1] for v in v_lakes]
ans.extend(v)

print(sum(v))
print(*ans)
