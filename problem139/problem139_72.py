def main():
    H1,M1,H2,M2,K = [int(x) for x in input().split()]
    if M2 >= M1:
        diff = (H2-H1)*60 + M2-M1
    else:
        diff = (H2-H1)*60 + 60-M1+M2 -60
    if diff <= 0:
        print(0)
    else:
        print(diff - K)

if __name__ == '__main__':
    main()
