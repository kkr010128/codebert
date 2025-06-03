def main():
  a,b= list(map(int,input().split()))
  a_str=""
  b_str=""
  for i in range(0,b):
    a_str+=str(a)
  for i in range(0,a):
    b_str+=str(b)
  
  if a_str<b_str:
    print(a_str)
  else:
    print(b_str)
main()