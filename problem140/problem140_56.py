T = input()
N = len(T)
after_T = ''

for i in range(N):
    charr=T[i]
    if(charr=='?'):
        after_T+='D'
    else:
        after_T+=charr

print(after_T)
