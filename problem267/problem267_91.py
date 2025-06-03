n = int(input())
s = input()

seen = {}

for i in range(n):
    if s[i] in seen:
        seen[s[i]].append(i)
    else:
        seen[s[i]] = [i]

cnt = 0

for a, ai in seen.items():
    for b, bi in seen.items():
        if ai[0] >= bi[-1]:
            continue

        lower = ai[0]
        upper = bi[-1]

        for c, ci in seen.items():
            search = ci
            if a == c:
                search = search[1:]
            if b == c:
                search = search[:-1]

            #binary search
            l = 0
            r = len(search)-1
            found = False

            while l <= r:
                mid = (l+r)//2

                if lower < search[mid] < upper:
                    found = True
                    break
                elif search[mid] >= upper:
                    r = mid-1
                else:
                    l = mid+1

            if found:
                cnt += 1

print(cnt)