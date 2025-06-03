H, W, K = list(map(int, input().split()))
c = []
for _ in range(H):
    c.append( input() )
count = 0
for h_pattern in range( 2**H ):
    for w_pattern in range( 2**W ):
        black_count = 0
        for h in range(H):
            for w in range(W):
                if (h_pattern>>h)&1 and (w_pattern>>w)&1 and c[h][w]=='#':
                    black_count+=1
        if black_count==K:
            count += 1
print(count)
