def main():
  input()
  A = list(map(int, input().split()))
  cusum = [0] * len(A)
  cusum[-1] = A[-1]

  if A[0] > 1:
    print(-1)
    return

  for i in range(len(A)-2, -1, -1):
    cusum[i] = cusum[i+1] + A[i]

  pre_node = 1
  ans = 1
  for i in range(1, len(A)):
    node = (pre_node - A[i-1]) * 2

    if node < A[i]:
        print(-1)
        return

    pre_node = min(node, cusum[i])
    ans += pre_node

  print(ans)

if __name__ == '__main__':
  main()
    
