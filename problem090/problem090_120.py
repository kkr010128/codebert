str=input()
maxcnt=0
cnt=0
for i in range(len(str)):
  if(str[i]=="R"):
    cnt+=1
    maxcnt=max(cnt,maxcnt)
  else:
    cnt=0
    
print(maxcnt)
