n=int(input())
s=input() 
mid=n//2
if(s[:mid]==s[mid:]):
  print("Yes")
else:
  print("No")
