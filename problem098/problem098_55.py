def main(s):
  a = 0 #r-w 
  b = 0 #w-r 
  for i in s:
    if i == "R":
      a += 1
  ans = max(a,b) #無しもしない場合操作最大値 
  for i in s:
    if i == "R":
      a -= 1
    else:
      b += 1
    now = max(a,b)
    ans = min(ans, now)
  print(ans)
  
if __name__ == '__main__':
  n = int(input())
  s = input()
  main(s)