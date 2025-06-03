
s = input()
prev = 'D'
ans = []

for i in s:
    if(i=='P' or i=='D'):
        prev=i
        ans.append(i)
    else:
        ans.append('D')

print(''.join(ans))

