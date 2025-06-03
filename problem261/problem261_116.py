s = input()
sa = s[:len(s)//2]
if len(s)%2 == 0:
    sb = s[len(s)//2:]
if len(s)%2 == 1:
    sb = s[len(s)//2+1:]

sbr = sb[::-1]
cnt = 0
for i in range(len(sa)):
    if sa[i] != sbr[i]:
        cnt+=1

print(cnt)