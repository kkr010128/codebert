def main():
  s=input()
  x=s[:int((len(s)-1)/2)]
  y=s[int((len(s)+3)/2)-1:]
  flg=0
  
  if s !=s[::-1]:
    flg=1
  if x !=x[::-1]:
    flg=1
  if y !=y[::-1]:
    flg=1
  if flg==1:
    print("No")
  else:
    print("Yes")
main()