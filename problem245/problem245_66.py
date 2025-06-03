n=input()
s1= input()

count=0
for i in range(len(s1)-2):
    if(s1[i]=='A' and  s1[i+1]=='B' and s1[i+2]=='C'):
        count=count+1

print(count)