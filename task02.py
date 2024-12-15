import logging
from abc import ABC, abstractmethod

# Налаштування логування
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f"Книга додана: {book}")

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]
        logger.info(f"Книга з назвою '{title}' видалена")

    def show_books(self) -> None:
        if self.books:
            for book in self.books:
                logger.info(book)
        else:
            logger.info("У бібліотеці немає книг.")


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            manager.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            break
        else:
            logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
