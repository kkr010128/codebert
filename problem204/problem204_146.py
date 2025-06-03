S = input()
Q = int(input())
reverse = False
before = []
after = []
for i in range(Q):
    q = input().split()
    if len(q) == 1:
        reverse = not reverse
    else:
        T, F, C = q
        if (F == '1' and not reverse) or (F == '2' and reverse):
            before.append(C)
        else:
            after.append(C)

if not reverse:
    answer = ''.join(before[::-1]) + S + ''.join(after)
else:
    answer = ''.join(after[::-1]) + S[::-1] + ''.join(before)
print(answer)