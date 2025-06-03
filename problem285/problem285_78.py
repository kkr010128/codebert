a=list(input())
count=1
ans = 0
temp = 0
for i in range(len(a)-1):
  if a[i] ==a[i+1]:
    count+=1
  else:
    if a[i]=='<':
      ans += count*(count+1)//2
      temp = count
      #print('<', count, ans)
      count = 1
      
    else:
      ans += count*(count+1)//2
      ans -= min(count, temp)
      #print('>', count, ans)
      count =1
else:
  if a[-1]=='<':
    ans += count*(count+1)//2
  else:
    ans += count*(count+1)//2
    ans -= min(count, temp)
print(ans)