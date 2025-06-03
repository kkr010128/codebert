if __name__ == "__main__":
    N = int(input())
    hash = {}
    for i in range(N):
        hash[input()] = ""
    print(len(hash.keys()))