from sys import stdin, stdout # only need for big input

def solve():
    s = input() 
    left = 0
    right = len(s) - 1
    count = 0
    while left < right:
        count += (s[left] != s[right])
        left += 1
        right -= 1
    print(count)

def main():
    solve()


if __name__ == "__main__":
    main()