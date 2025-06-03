n = int( input() )
x = input()
x_pop = x.count( "1" )
x_pls = x_pop + 1
x_mns = x_pop - 1

# 2の冪乗のリスト．ただし後々に備えてpopcountで割った余りにしてある
rp = [ pow( 2, i, x_pls ) for i in range( n + 1 ) ]
if x_mns > 0:
    rm = [ pow( 2, i, x_mns ) for i in range( n + 1 ) ]
else:
    rm = [ 0 ] * ( n + 1 )

x = x[ : : -1 ]
rem_p = 0
rem_m = 0
for i in range( n ):
    if x[ i ] == "1":
        rem_p += rp[ i ]
        rem_m += rm[ i ]

for i in range( n - 1, -1, -1 ):
    if x[ i ] == "0":
        tmp = ( rem_p + rp[ i ] ) % x_pls
    elif x_mns > 0:
        tmp = ( rem_m - rm[ i ] ) % x_mns
    else: # popcount( X_i ) == 0
        print( 0 )
        continue
    ans = 1
    while tmp > 0:
        tmp = tmp % bin( tmp ).count( "1" )
        ans += 1
    print( ans )