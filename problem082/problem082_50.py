s = input()
t= input()
c=0
an = 10**8
for i in range(len(s)-len(t)+1):
    for j in range(i,i+len(t)):

        if s[j]!=t[j-i]:
            c+=1

    an = min(c,an)
    c=0
print(an)
