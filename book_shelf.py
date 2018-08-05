# -*- coding: utf-8 -*-


class BookShelf(object):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__books = {}

    def __get_space(self):
        return self.__width - sum([book.width for book in self.__books.values()])

    def add_book(self, book):
        if not self.is_add_book(book):
            return False
        self.__books[book.name] = book
        return True

    def take_book(self, book_name):
        if self.is_book(book_name):
            return None
        return self.__books.pop(book_name)

    def is_add_book(self, book):
        if book.height >= self.__height:
            return False
        if book.width >= self.__get_space():
            return False
        return True

    def is_book(self, book_name):
        return book_name in self.__books


if __name__ == '__main__':
    pass
