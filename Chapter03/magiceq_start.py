# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    # Overide __eq__
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return (self.title == value.title and 
            self.author == value.author and self.price == value.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    # Override __gt__
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price >= value.price

    # TODO: the __lt__ establishes < relationship with another obj
    # Override __lt__
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price < value.price

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
# note comparing instance to instance not values per se
print( b1 == b3 )
# print(b1.__eq__(b3)) # this calls the magic __eq__ explicitly
print( b1 == b2 )
# print( b1 == 42 )

# TODO: Check for greater and lesser value
print( b2 >= b1 )
print( b2 < b1 )

# TODO: Now we can sort them too
books = [b1, b3, b2, b4]
books.sort() # uses the __lt__ 
print([book.title for book in books])