h = int(input())
w = int(input())
n = int(input())

n_push = []

for n_h in range(h+1):
  for n_w in range(w+1):
    n_tmp = (n_h)*w + (n_w)*h - ((n_h)*(n_w))

    if n_tmp>=n:
      n_push.append(n_h + n_w)

print(min(n_push))