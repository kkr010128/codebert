def main():
  s = input()
  t = input()
  t = t[0:len(t)-1]
#  print(s,t)
  ans = 'Yes' if s == t else 'No'
  print(ans)
  
if __name__ == '__main__':
  main()
