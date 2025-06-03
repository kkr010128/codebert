#! python3
# coding:utf-8
import collections
 
def main():
    n = int(input())
    slist = [input() for _ in range(n)]
    c = collections.Counter(slist)
    print(len(c))

if __name__ == "__main__":
    main() 