# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount     # '_' is a private convention, since python does not have private

# TODO: create some book instances
b1 = Book("War and Peace","Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye","JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(round(b2.getprice(),2))


# TODO: properties with double underscores are hidden by the interpreter
# print(b2.__secret) # this will error out
print(b2._Book__secret) # this is a workaround