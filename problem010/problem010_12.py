def insertionSort(a, n):
  print " ".join(map(str, a))
  for i in xrange(1, n):
    v = a[i]
    j = i - 1
    # print "i = " + str(i) + ", j = " + str(j)
    while j >= 0 and v < a[j]:
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = v
    print " ".join(map(str, a))

n = int(raw_input())
a = map(int, raw_input().split(" "))
insertionSort(a, n)