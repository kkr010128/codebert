from string import ascii_lowercase
N = int(input())
ans = ['a']
for i in range(1, N):
    ans2 = []
    for a in ans:
        for b in ascii_lowercase[:len(set(a)) + 1]:
            ans2 += [a + b]
    ans = ans2
print('\n'.join(ans))
