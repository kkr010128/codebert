S , T  = input().split()
A , B =map(int,input().split())
U = input()

mydict = {S:A, T:B}

mydict[U] -= 1
print ( str( mydict[S] ) + " " +str( mydict[T] )  )

