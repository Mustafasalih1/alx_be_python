class Book:
    def __init__(self, title, author, year):
        self.title = tiltle
        self.author = author
        self.year = year

    def __str__(self):
        return f"(title) by (author), published in (year)"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        return f"Deleting (title of the book)"