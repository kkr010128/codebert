import itertools

for i in itertools.count ( 1 ):
  d = int ( input ( ) )
  if d == 0:
    break
  print ( "Case %s: %s" % ( i, d ) )