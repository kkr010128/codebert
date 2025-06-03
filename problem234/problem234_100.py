
def main():
    N = int(input())
    NN = [[0]*10 for _ in range(11)]
    for i in range(11,100):
        As = str(i)[0]
        Ae = str(i)[-1]
        cnt = 0
        for j in range(1,N+1):
            if str(j)[-1]== As and str(j)[0] == Ae:
                cnt +=1
        NN[int(As)][int(Ae)] = cnt


    ans = 0
    for i in range(1,N+1):
        ans += NN[int(str(i)[0])][int(str(i)[-1])]

    print(ans)

if __name__ == '__main__':
        main()

