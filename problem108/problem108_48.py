def main(N):
    surplus = N%1000
    if surplus == 0:
        return 0
    else:
        ans = 1000 - surplus
        return ans

if __name__ == '__main__':
    N = int(input())
    ans = main(N)
    print(ans)

