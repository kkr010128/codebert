def calc_number_of_coin(sum, coins):
    dp = [999999999]*(sum+1)
    dp[0] = 0
    for i in range(len(coins)):
        for j in range(coins[i], sum+1):
            dp[j] = min(dp[j], dp[j-coins[i]]+1)
    return dp[sum]



if __name__ == '__main__':
    # ??????????????\???
    # f = open('input.txt')
    # sum, _ = [int(x) for x in f.readline().strip().split(' ')]
    # coins = [int(x) for x in f.readline().strip().split(' ')]

    sum, _ = [int(x) for x in input().strip().split(' ')]
    coins = [int(x) for x in input().strip().split(' ')]

    # ???????????????
    result = calc_number_of_coin(sum, coins)

    # ???????????¨???
    print(result)