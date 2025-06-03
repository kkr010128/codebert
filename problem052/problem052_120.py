import sys

def main():
    lines = sys.stdin.readlines()
    input_num = 0
    ans = []
    for line in lines:
        # print(line)
        # rm '\n' from string of a line
        line = line.strip('\n')
        input_num = int(line)
        n = input_num
        # print input_num
        print "",
        index_num = 1
        flag = 0
        while True:
            # END CHECKNUM
            if index_num != 1 or flag == 1:
                if (index_num + 1) > n:
                    break
                else:
                    index_num += 1 # Go on below
            else:
                flag = 1
            x = index_num
            if x % 3 == 0:
                print index_num,
                continue
            if x % 10 == 3:
                print index_num,
                continue
            else:
                while x > 0:
                    x /= 10
                    if x % 10 == 3:
                        print index_num,
                        break

        break


if __name__ == "__main__":
    main()