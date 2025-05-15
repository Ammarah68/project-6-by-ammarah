class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

book1 = Book("The CountDown Book")
book2 = Book("Physics for 10")
book3 = Book("Oxford Science 8")

print("Total number of books:", Book.total_books)
