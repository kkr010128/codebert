n = list(str(input()))
flag = False
for i in range(len(n)):
    if n[i] == '7':
        flag = True
if flag:
    print('Yes')
else:
    print('No')
