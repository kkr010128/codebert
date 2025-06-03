def mapt(fn, *args):
    return tuple(map(fn, *args))

def main():
    n, k = mapt(int, (input().split(" ")))
    a = sorted(mapt(int, input().split(" ")))
    if k >= len(a): print(0); exit()
    while k > 0:
        a.pop()
        k -= 1
    print(sum(a))
    
main()