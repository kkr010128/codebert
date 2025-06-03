def main():  
  x = int(input())
  a = 1
  while True:
    c = a**5
    for b in range(-a,a+1):
      d = c - b**5
      if d == x:
        print(a,b)
        return
      if d == -x:
        print(b,a)
        return
    a+=1
  
if __name__ == "__main__":
  main()