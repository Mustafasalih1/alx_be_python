class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """Represents a library containing a collection of books."""

    def __init__(self):
        self._books = []  

    def add_book(self, book):
        """Add a new Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Find a book by title and check it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True  
        return False  

    def return_book(self, title):
        """Find a book by title and return it (mark as available)."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True  
        return False  

    def list_available_books(self):
        """Print the list of available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")