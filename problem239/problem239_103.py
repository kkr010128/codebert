import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    c = input().strip()

    print(alphabet[alphabet.index(c) + 1])


main()