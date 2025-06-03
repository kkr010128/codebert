def count_rainy(weather): 
    if weather == 'RSR':
        return 1
    return len([r for r in weather if r == 'R'])

weather = input()
print(count_rainy(weather))