def main():
    # データ入力
    n, q = input().split()
    n = int( n )
    q = int( q )
    name = []
    time = []
    for i in range(n):
        tmp_n, tmp_t = input().split()
        name.append( tmp_n )
        time.append( int( tmp_t ) )

    # 処理
    count = 0
    while n > 0:
        if time[0] > q:
            time[0] -= q
            count += q
            time.append( time[0] )
            time.pop( 0 )
            name.append( name[0] )
            name.pop( 0 )
        else :
            count += time[0]
            print( name[0], end=" " )
            print( str( count ) )
            time.pop( 0 )
            name.pop( 0 )
            n -= 1

if __name__ == '__main__':
    main()

