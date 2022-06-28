with open("./week_11/books.txt") as books:
    for book in books:
        book = book.strip()
        print(book)
