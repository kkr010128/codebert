_ = int(input())
hoge = [int(x) for x in input().split()]
_ = int(input())

def exSearch(i, m):
    if m == 0:
        return True
    if i >= len(hoge) or m > sum(hoge):
        return False
    res = exSearch(i+1, m) or exSearch(i+1, m-hoge[i])
    return res

if __name__ == '__main__':
    
    for val in (int(x) for x in input().split()):
        if exSearch(0, val):
            print ('yes')
        else:
            print ('no')
