def main():
  N=int(input())
  print(sum([(N-1)//a for a in range(1,N)]))
  
if __name__=="__main__":
  main()