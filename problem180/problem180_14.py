n,k = map(int,input().split())

if n < k:
    rival_n = k - n
    if n >= rival_n:
      print(rival_n)
    else:
      print(n)

elif n == k:
    print(0)

else:

    n = n % k
    rival_n = k - n
    if n >= rival_n:
        print(rival_n)
    else:
        print(n)
