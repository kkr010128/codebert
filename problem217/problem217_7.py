n = input()

l = list( map(int, input().split()))

odd = [ c for c in l if (c % 2 == 0 ) and (( c % 3 != 0) and ( c % 5 !=0 ))]
if len( odd ) == 0: 
  print( "APPROVED" )
else:
  print( "DENIED" )