def check(seq):
    return len(seq) != len(set(seq))

def main():
  N = int(input())
  A = list(map(int, input().split()))
  ans = check(A)
  if ans:
    print("NO")
  else:
    print("YES")
main()