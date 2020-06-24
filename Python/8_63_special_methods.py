# What if you want to read the length of your own class for some reason?

class Book():
    """docstring for Book."""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

b = Book("A book", "meee", 200)

# If you do this:
print(str(b))
# It doesnt give what you would expect, it gives the memory location of the class
# soooo, add the __str__ to the class
