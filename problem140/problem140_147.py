t = input()
ans = []
for i in range(len(t)):
    if t[i] == '?':
        ans.append('D')
    else:
        ans.append(t[i])
print(''.join(ans))