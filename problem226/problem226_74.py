H, N = map(int, input().split())
special_move = input().split()
def answer(H: int, N: int, special_move: list) -> str:
    damage = 0
    for i in range(0, N):
        damage += int(special_move[i])
    if damage >= H:
        return 'Yes'
    else:
        return 'No'
print(answer(H, N, special_move))