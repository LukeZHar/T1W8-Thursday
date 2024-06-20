class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title='{self.title}' by '{self.author}', year={self.year})"
    
# Creating an instance of book
book1 = Book('War and Peace', 'Leo Tolstoy', 1869)

# Using repr to get the string representation
print(repr(book1))

# Printing the object directly also calls __repr__
print(book1)