import sys

input = sys.stdin.readline

def main():
    s = input().rstrip('\n')
    n = len(s)
    ansl = [0]*(n+1)
    for i in range(n):
        if s[i] == '<':
            ansl[i+1] = ansl[i]+1
    for i in reversed(range(n)):
        if s[i] == '>':
            ansl[i] = max(ansl[i+1]+1,ansl[i])
    print(sum(ansl))

if __name__ == '__main__':
    main()