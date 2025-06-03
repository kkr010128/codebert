N = int(input())
S = input()
ans = ['' for _ in range(len(S))]
a = ord('A')
for i, c in enumerate(S):
    ans[i] = chr((ord(c) - a + N) % 26 + a)
print(''.join(ans))