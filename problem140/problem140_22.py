t = input()
if(len(t) == 1):
    if (t[0] == '?'): t = "D"
if(t[0] == '?'):
    if  (t[1] == 'D'): t = "".join(['P' , t[1:]])
    elif(t[1] == '?'): t = "".join(['PD', t[2:]])
    else:              t = "".join(['D' , t[1:]])
if(t[-1] == '?'):
    t = "".join([t[:-1], 'D'])
for i in range(len(t)-1):
    if(t[i] == '?'):
        if(t[i-1] == 'P'):    t = "".join([t[:i], 'D' , t[i+1:]])
        elif(t[i+1] == 'D'):  t = "".join([t[:i], 'P' , t[i+1:]])
        elif(t[i+1] == 'P'):  t = "".join([t[:i], 'D' , t[i+1:]])
        elif(t[i+1] == '?'):  t = "".join([t[:i], 'PD', t[i+2:]])
print(t)