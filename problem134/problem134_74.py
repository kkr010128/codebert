if __name__ == '__main__':
  n = int(input())
  a = input().split()
  a = [int(x) for x in a]
  ans = 1

  if 0 in a:
        print(0)
  else:
      for i in a:
        ans = ans*i
        if ans > 10**18:
            ans = -1
            break
      print(ans)