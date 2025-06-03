my_str = input()

s1 = []
s2 = []
sum = 0

for idx, letter in enumerate(my_str):
    if letter == '\\':
        s1.append(idx)

    elif letter == '/' and s1:
        jdx = s1.pop()
        a = idx -jdx
        sum += a

        while s2 and s2[-1][0] > jdx:
            a += s2.pop()[1]
        s2.append([jdx, a])

print(sum)
print(len(s2), *(a for _, a in s2))
