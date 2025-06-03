string = input()
q = int(input())
for i in range(q):
  order = list(input().split())
  a, b = int(order[1]), int(order[2])
  if order[0] == "print":
    print(string[a:b+1])
  elif order[0] == "reverse":
    string = string[:a] + (string[a:b+1])[::-1] + string[b+1:]
  else:  
    string = string[:a] + order[3] + string[b+1:]
