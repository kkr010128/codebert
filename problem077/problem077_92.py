# coding: utf-8
# Your code here!

def main():
    a, b, c, d = map(int, input().split())
    
    ans = max(a*c, max(b*d, max(a*d, b*c)))
    
    print(ans)

main()
