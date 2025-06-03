if __name__ == "__main__":
    while True:
        nums = map( int, raw_input().split())
        H = nums[0]
        W = nums[1]
        if H == 0:
            if W == 0:
                break

        s = ""
        j = 0
        while j < W:
            s += "#"
            j += 1

        i = 0
        while i < H:
            print s
            i += 1
        print