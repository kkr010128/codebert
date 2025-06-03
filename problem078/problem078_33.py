def main():
  N=int(input())
  m=int(1e9+7)
  print((pow(10,N,m)-pow(9,N,m)-pow(9,N,m)+pow(8,N,m))%m)
if __name__=='__main__':
  main()
