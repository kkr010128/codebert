#   ==========     //\\       //||     ||====//||
#       ||        //  \\        ||     ||   // ||
#       ||       //====\\       ||     ||  //  ||
#       ||      //      \\      ||     || //   ||
#   ========== //        \\  ========  ||//====|| 
#  code

# 1 -> 1,2 2,1 3,
# 2 -> 1,1
def solve():
    n = int(input())
    cnt = 0
    for i in range(1, n + 1):
        k = n // i
        if n % i:
            cnt += k
        else:
            cnt += max(0, k - 1)
    print(cnt)
    return

def main():
    t = 1
    # t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()