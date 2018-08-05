# -*- coding: utf-8 -*-
from book_shelf import BookShelf
from book import Book
import random


class BookMachine(object):
    def __init__(self, shelf_list):
        self.__shelf_list = shelf_list

    def __loop_shelf(self, func, book):
        """
        :param func: 実行する関数
        :param book: 本クラス
        :return:
        """
        result = None
        for shelf in self.__shelf_list:
            result = func(shelf, book)
            if result:
                return result
        return result

    @staticmethod
    def __add(shelf, book):
        return shelf.add_book(book)

    @staticmethod
    def __take(shelf, book):
        return shelf.take_book(book)

    def take_book(self, book):
        return self.__loop_shelf(self.__take, book)

    def add_book(self, book):
        return self.__loop_shelf(self.__add, book)


if __name__ == '__main__':

    book_list = [Book('hoge', 15, 2),
                 Book('hige', 15, 5),
                 Book('hage', 14, 3),
                 Book('hege', 15, 6),
                 Book('huge', 30, 5),
                 Book('fuga', 15, 4),
                 Book('fuge', 15, 2),
                 Book('fugi', 20, 8),
                 Book('fugo', 15, 4),
                 Book('fugu', 18, 2)]
    book_dict = {b.name: b for b in book_list}

    shelfs = [BookShelf(25, 40)]
    info_txt = ('以下のコマンドから選択してください。\n'
                '1: 本棚に収納\n'
                '2: 本棚から取得\n'
                '3: 本棚ますぃーーーーんの終了\n'
                'Command: ')
    books = {}
    machine = BookMachine(shelfs)
    while True:
        print(info_txt)
        command = input().strip()
        if command == '3':
            break
        if command not in ('1', '2'):
            continue
        book_name = input('本の名前を入力してください: ')
        _book = book_dict.get(book_name)
        if _book is None:
            print('そんな本はない。')
            continue
        if command == '1':
            print('収納しました。' if machine.add_book(_book) else '収納できませんでした。')
        if command == '2':
            print('本を取り出しました。' if machine.take_book(book_name) else '本がありません。')
