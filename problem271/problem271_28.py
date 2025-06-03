n=int(input())
s=input()
S=[]
for i in s:
    if ord(i)+n > 90:
        S.append(chr(ord(i)+n-26))
    else:
        S.append(chr(ord(i)+n))
print(''.join(S))