def solve(h, w):
    print('#'*w,end='')
    print(('\n#'+'.'*(w-2)+'#')*(h-2))
    print('#'*w)
    print()

if __name__ == '__main__':
    while True:
        h, w = [int(i) for i in input().split()]
        if h == w == 0: break
        solve(h, w)