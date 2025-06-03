ary = list(input())
s1 = []
s = 0

s2 = []

cnt = 0
for _ in ary:

    if _ == '\\':
        s1.append(cnt)
        cnt += 1

    elif _ == '/':
        if s1:
            old_cnt = s1.pop()
            area = cnt - old_cnt
            s += area

            while s2:
                if old_cnt < s2[-1][0]:
                    area += s2.pop()[1]
                else:
                    break

            s2.append((old_cnt, area))

        cnt += 1

    else:
        cnt += 1

print(s)
print(len(s2), *[_[1] for _ in s2])
