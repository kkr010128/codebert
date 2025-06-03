def myAnswer(a:int,b:int,c:int) -> str:
   A = ( a + b - c) ** 2
   B = 4 * a * b

   return "Yes" if( A - B > 0 and (c - a - b) > 0) else "No"

def modelAnswer():
   return
def main():
   a,b,c = map(int,input().split())
   print(myAnswer(a,b,c))

if __name__ == '__main__':
   main()