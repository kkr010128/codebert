n = input()
a = map(int,raw_input().split())

for i in xrange(len(a)):
  v = a[i]
  j = i - 1
  while j >= 0 and a[j] > v :
    a[j+1] = a[j]
    j = j - 1
  a[j+1] = v

  print " ".join(map(str,a))