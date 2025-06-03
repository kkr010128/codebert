def greedy_sche(read_dir=1):
    res = []
    i = 1 if read_dir == 1 else n 
    cnt = 1
    while cnt <= k:
        if s[i - 1]:
            res.append(i)
            cnt += 1
            i += read_dir * (c + 1)
        else:
            i += read_dir
    return res


n, k, c = map(int, input().split())
s = [c == 'o' for c in input()]
[print(f) for f, b in zip(greedy_sche(1), greedy_sche(-1)[::-1]) if f == b]        
