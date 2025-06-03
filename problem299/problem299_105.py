def main():
   n = int(input())
   a = list(map(int,input().split()))
   b = [(0,0) for i in range(n)]
   for i in range(n):
       b[i] = (a[i],i + 1)
   b.sort()
   for i in range(n):
       if i != n - 1:
           print(b[i][1],end = " ")
       else:
           print(b[i][1])

main()