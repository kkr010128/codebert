if __name__ == "__main__":
    
    n = int(input())
    ops = []
    words = []
    for _ in range(n):
        op, word = input().split()
        ops.append(op)
        words.append(word)
    
    db = set()
    for op, word in zip(ops, words):
        if op=='insert':
            db.add(word)
        else:
            if word in db:
                print("yes")
            else:
                print("no")

