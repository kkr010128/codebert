cards = {
        'S': [0 for _ in range( 13)],
        'H': [0 for _ in range( 13)],
        'C': [0 for _ in range( 13)],
        'D': [0 for _ in range( 13)],
        }

n = int( input())
for _ in range( n):
    (s, r) = input().split()
    r = int(r)
    cards[s][r - 1] = r

for s in ( 'S', 'H', 'C', 'D'):
    for r in range( 13):
        if cards[s][r] == 0:
            print( '{0:s} {1:d}'.format( s, r+1))