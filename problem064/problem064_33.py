s=[ord(i) for i in input()]
n=[ord(i) for i in input()]
flag=0
flack=0
for i in range(len(s)):
    flack=0
    if n[0]==s[i]:
        flack=1
        for j in range(1,len(n)):
            if i+j>=len(s):
                if n[j]==s[i+j-len(s)]:
                    flack=flack+1
                else:
                    break
            else:
                if n[j]==s[i+j]:
                    flack=flack+1
                else:
                    break
    if flack==len(n):
        flag=1
        break
                
if flag:
    print('Yes')
else:
    print('No')