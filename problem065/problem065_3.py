s=input().lower()
cnt=0
while True:
    l=input().split()
    if l[0]=='END_OF_TEXT': break
    for i in range(len(l)):
        lg=len(l[i])-1
        if not l[i][lg].isalpha(): l[i]=l[i][:lg]
        cnt+=(s==l[i].lower())
print(cnt)