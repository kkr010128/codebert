n = -100, -100

while n[0] != 0 or n[1] != 0:
   n = map( int, raw_input().split())
   if n[0] != 0 or n[1] != 0:
      print min(n[0],n[1]),max(n[0],n[1])