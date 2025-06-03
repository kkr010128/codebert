if __name__ == '__main__':
    x, y = map(int, input().split())
    ans = 'No'
    for i in range(x+1):
        legs = 4*i+2*(x-i)
        
        if legs == y:
            ans = 'Yes'
            break

    print(ans)