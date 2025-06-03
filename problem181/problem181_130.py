def main():
    k = int(input())
    if k<10:
        print(k)
        return
    que = [i for i in range(1,10)]
    cnt = 0
    while True:
        q = que.pop(0)
        cnt += 1
        if cnt==k:
            print(q)
            return
        if q%10==0:
            que.append(q*10)
            que.append(q*10+1)
        elif q%10==9:
            que.append(q*10+9-1)
            que.append(q*10+9)
        else:
            que.append(q*10+q%10-1)
            que.append(q*10+q%10)
            que.append(q*10+q%10+1)

if __name__ == "__main__":
    main()
