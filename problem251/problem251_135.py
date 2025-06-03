def main():
  N, K = map(int, input().split())
  R, S, P = map(int, input().split())
  T = input()

  l = ["" for i in range(K)]
  s = 0
  for i in range(N):
    # print(l)
    if l[i%K] == T[i]:
      l[i%K]=""
      continue

    if l[i%K] == "":
      if T[i] == "r":
        s = s+P
        l[i%K] = "r"
      elif T[i] == "s":
        s = s+R
        l[i%K] = "s"
      else:
        s = s+S
        l[i%K] = "p"

    elif T[i]=="r":
      s = s+P
      l[i%K] = "r"
    elif T[i]=="s":
      s = s+R
      l[i%K] = "s"
    else:
      s = s+S
      l[i%K] = "p"

  print(s)

if __name__ == "__main__":
    main()