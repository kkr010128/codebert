t = input()
le = len(t)
tt = []
for i in range(le):
    c = t[i]
    if t[i] == '?':
        c = 'D'
        if i > 0 and tt[i - 1] == 'P':
            c = 'D'
        elif i == 0 and le > 1 and t[i + 1] == 'D' or i == 0 and le > 1 and t[i + 1] == '?':
            c = 'P'
        elif i < le - 1 and t[i + 1] == 'D' or i < le - 1 and t[i + 1] == '?':
            c = 'P'
    tt.append(c)
print(''.join(tt))