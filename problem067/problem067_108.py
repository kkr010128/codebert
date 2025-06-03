def main():

    match_count = int(input())
    matches = [input().split() for i in range(match_count)]
    
    taro_result = [3 if match[0] > match[1] else 1 if match[0] == match[1] else 0 for match in matches]
    print('%d %d' % (sum(taro_result), sum(3 if item == 0 else 1 if item == 1 else 0 for item in taro_result)) )


main()