s=input()
s_list=list(s)
s_list.append('0')
for i in range(len(s)):
  if s_list[i]=='?':
    if s_list[i+1]=='D':
      if s_list[i-1]=='P':
        s_list[i]='D'
      else:
        s_list[i]='P'
    elif s_list[i+1]=='?':
      if s_list[i-1]=='P':
        s_list[i]='D'
      else :
        s_list[i]='P'
    else :
      s_list[i]='D'
    
    
s_list.pop()
a="".join(s_list)
print(a)