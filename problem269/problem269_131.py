def main():
    T1,T2 = map(int,input().split())
    A1,A2 = map(int,input().split())
    B1,B2 = map(int,input().split())

    move = T1*(A1-B1) + T2*(A2-B2)
    mid = T1*(A1-B1)

    if move==0:
        return -1

    if move*mid > 0:
        return 0

    if move < 0:
        move *= -1
    else:
        mid *= -1

    if mid%move == 0:
        return 2*(mid//move)
    else:
        return 2*(mid//move)+1

if __name__ == "__main__":
    ans = main()
    if ans==-1:
        print("infinity")
    else:
        print(ans)
