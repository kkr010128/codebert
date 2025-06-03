hp1, atk1, hp2, atk2 = map(int, input().split())

print("Yes" if hp2 / atk1 <= -(-hp1 // atk2) else "No")