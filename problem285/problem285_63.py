import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = input()
    ans, i, j = 0, 0, 0
    while i < len(s):
        if s[i] == '<':
            j = 0
            while i<len(s) and s[i] == '<':
                ans += j
                j += 1
                i += 1
        else:
            k = 1
            while i<len(s) and s[i] == '>':
                ans += k
                k += 1
                i += 1
            if j > k - 1:
                ans = ans - (k - 1) + j
    if s[-1] == '<':
        ans += j
    print(ans)
                
            
if __name__ == '__main__':
    main()