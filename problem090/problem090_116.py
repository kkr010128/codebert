def check_weather(weathers: str) -> int:
    count = weathers.count('R')
    return 1 if weathers[1] == 'S' and count == 2 else count

if __name__=='__main__':
    print(check_weather(input()))