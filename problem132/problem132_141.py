def main():
    N_ko, K_kai = map(int, input().split())
    init_light = list(map(int, input().split()))


    for k in range(min(42,K_kai)):
        light_list = [0 for i in range(N_ko)]

        for i in range(N_ko):
            left = max(0, i - init_light[i])
            right = min(N_ko - 1, i + init_light[i])
            
            light_list[left] += 1

            if (right + 1 < N_ko):
                light_list[right + 1] -= 1
            
        for i in range(1, N_ko):
            light_list[i] += light_list[i - 1]
        
        init_light = light_list

    
    print(' '.join(map(str,light_list)))


if __name__ == '__main__':
    main()
