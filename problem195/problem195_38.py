import sys
# sys.stdin = open('input.txt')

k = int(input())
string = '1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51'
s = [i for i in map(int, string.split(', '))]
print(s[k-1])