def triangle(N, Ls):
  result = 0
  res = []
  numbers = {}
  edgeLength = list(set(Ls))
  for i in edgeLength:
    numbers[i] = Ls.count(i)
  for i in range(len(edgeLength)):
    a = edgeLength[i]   
    copy1 = edgeLength[i+1:]
    for j in range(len(copy1)):
      b = copy1[j]
      copy2 = copy1[j+1:]
      for k in range(len(copy2)):
        c = copy2[k]
        if a + b > c and b + c > a and c + a > b:
          res.append([a, b, c])
  for val in res:
    result += numbers[val[0]] * numbers[val[1]] * numbers[val[2]]
  return result




if __name__ == "__main__":
  N = list(map(int, input().split()))
  Ls = list(map(int, input().split()))
  print(triangle(N, Ls))
