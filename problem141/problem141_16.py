def main():
  input()
  in_a = list(map(int, input().split()))
  leaves = [0] * len(in_a)
  leaves[-1] = in_a[-1]

  if in_a[0] > 1:
    print(-1)
    return

  #for i in range(len(in_a)-2, -1, -1):
  #  leaves[i] = leaves[i+1] + in_a[i]

  for i in range(len(in_a) - 1, 1, -1):
    leaves[i-1] = leaves[i] + in_a[i-1]
    
  node = 1
  total = 1
  
  for i in range(1, len(in_a)):
    n = (node - in_a[i-1]) * 2

    if n < in_a[i]:
        print(-1)
        return

    node = min(n, leaves[i])
    total += node

  print(total)

if __name__ == '__main__':
  main()
    
