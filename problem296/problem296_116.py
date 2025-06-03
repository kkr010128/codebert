import itertools
def main():
  S = input()
  K = int(input())
  
  if len(set(S)) == 1:
    print(len(S) * K // 2)
    return
  
  cc = 0
  gg = itertools.groupby(S)
  for key, item in gg:
    cc += len(list(item))//2
  a = b = 0
  if S[0] == S[-1]:
    while a < len(S) and S[a] == S[0]:
      a += 1
    S = S[::-1]
    while b < len(S) and S[b] == S[0]:
      b += 1
  output = K * cc - (K-1) * (a//2 + b//2 - (a+b)//2)
  print(output)
  return

if __name__ == '__main__':
  main()