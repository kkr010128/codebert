if __name__ == '__main__':
    p_taro, p_hanako = 0, 0
    n = int(input())
    for i in range(n):
        animal_taro, animal_hanako = input().split()
        if animal_taro > animal_hanako:
            p_taro += 3
        elif animal_taro < animal_hanako:
            p_hanako += 3
        else:
            p_taro, p_hanako = p_taro+1, p_hanako+1
    print(p_taro, p_hanako)