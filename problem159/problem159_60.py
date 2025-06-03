from math import floor

def main():
    X=int(input())
    tmp=100
    for year in range(1,4000):
        tmp += tmp//100
        if tmp >= X:
            print(year)
            exit()

main()
