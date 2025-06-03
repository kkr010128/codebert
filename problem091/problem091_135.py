n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            _lst = [l[i], l[j], l[k]]

            if len(set(_lst)) == 3:
                _max = max(_lst)
                _lst.remove(_max)
                if _max < sum(_lst):
                    ans += 1

print(ans)
