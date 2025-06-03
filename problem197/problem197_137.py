
def main():
 a,b,c = map(int,input().split())
 rhs = c - a - b
 lhs = 4 * a * b
 if rhs > 0  and lhs < rhs ** 2:
  print('Yes')
 else:
  print('No')
main()