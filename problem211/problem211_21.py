

def main():
  N,R=map(int,input().split())
  if(N<10):
    inner=R+100*(10-N)
  else:
    inner=R
  
  print(inner)

if __name__ == '__main__':
	main()