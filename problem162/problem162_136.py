N, M = map(int, input().split())
assert 2*M+1 <= N

if M % 2 == 1:
    step_m1 = M
    step_m2 = M - 1
else:
    step_m1 = M - 1
    step_m2 = M
assert step_m1 + 1 + step_m2 + 1 <= N
ans = []
a = 0
for step in range(step_m1, -1, -2):
#     print(step)
#     print(a, a+step)
    ans.append([a+1, a+step+1])
    a += 1
a = step_m1 + 1
for step in range(step_m2, 0, -2):
#     print(step)
#     print(a, a+step)
    ans.append([a+1, a+step+1])
    a += 1
print('\n'.join(map(lambda L: ' '.join(map(str, L)), ans)))