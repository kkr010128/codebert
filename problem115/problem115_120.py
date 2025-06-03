def resolve():
    a = int(input())
    ans = a * (1 + a * (1 + a))
    print(ans)

if __name__ == "__main__":
    resolve()