#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    string=""
    n = int(input())
    for i in range(n):
        string+="ACL"
    print(string)


if __name__=="__main__":
    main()