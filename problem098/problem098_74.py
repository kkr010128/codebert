def main():
    N = int(input())
    C = list(input())
    C_ = sorted(C)

    wr = rw = 0
    for i in range(len(C_)):
        if C[i] != C_[i]:
            if C[i] == "R" and C_[i] == "W":
                rw += 1
            else:
                wr += 1

    print(max(wr, rw))
    
if __name__ == "__main__":
    main()