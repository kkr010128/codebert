# https://atcoder.jp/contests/abc172/tasks/abc172_a

def calc(a):
    return a + (a ** 2) + (a ** 3)

a = int(input())
print(calc(a))