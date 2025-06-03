def backtrack(books, cur_book_ids, threshold, result):
    if len(cur_book_ids) > len(books):
        return
    if len(cur_book_ids) == len(books):
        achieved = True
        price_skills = [0] * len(books[0])
        for book,is_bought in zip(books, cur_book_ids):
            for j in range(len(book)):
                price_skills[j] += book[j]*is_bought
        for i in range(1, len(price_skills)):
            if price_skills[i] < threshold:
                achieved = False
        if achieved:
            if not result:
                result.append(price_skills[0])
            else:
                result[0] = min(result[0], price_skills[0])

    for i in (0,1):
        cur_book_ids.append(i)
        backtrack(books, cur_book_ids, threshold, result)
        cur_book_ids.pop()

def solve():
    N,M,X = [int(i) for i in input().split()]
    books = []
    for i in range(N):
        book = [int(i) for i in input().split()]
        books.append(book)
    result = []
    backtrack(books, [], X, result)
    if not result:
        print(-1)
    else:
        print(result[0])

if __name__ == "__main__":
    solve()