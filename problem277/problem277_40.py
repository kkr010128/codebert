def main():
    height, width, strawberries = map(int, input().split())
    cake = [list(input()) for _ in range(height)]
    answer = [[0 for _ in range(width)] for _ in range(height)]
    strawberry_num = 0
    for i in range(height):
        is_exist_strawberry = False
        for j in range(width):
            if cake[i][j] == "#":
                is_exist_strawberry = True
                strawberry_num += 1
                answer[i][j] = strawberry_num
            elif is_exist_strawberry:
                answer[i][j] = strawberry_num
    row_with_strawberry = -1
    for i in range(height):
        before_index = 0
        for j in range(-1, -width - 1, -1):
            if answer[i][j] == 0:
                answer[i][j] = before_index
            else:
                before_index = answer[i][j]
                if row_with_strawberry == -1:
                    row_with_strawberry = i
    for i in range(row_with_strawberry):
        answer[i] = answer[row_with_strawberry]
    for i in range(row_with_strawberry, height):
        if answer[i][0] == 0:
            answer[i] = answer[i - 1]
    for ans in answer:
        print(" ".join(map(str, ans)))


if __name__ == '__main__':
    main()

