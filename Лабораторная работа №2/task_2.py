BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]



class Book:
    """ Класс для создания книги """

    def __init__(self, id_: int, name: str, pages: int):
        """
        Иницилизирует объект Book

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not id_ > 0:
            raise ValueError("id_ должен быть положительный")
        if not isinstance(id_, int):
            raise TypeError("id_ должен быть только целым числом")
        self.id_ = id_
        if not isinstance(name, str):
            raise TypeError("name должен быть строковым типом данных")
        self.name = name
        if not pages > 0:
            raise ValueError("pages должен быть положительный")
        if not isinstance(pages, int):
            raise TypeError("pages должен быть только целым числом")
        self.pages = pages


class Library:
    """ Класс для создания библиотеки книг """
    def __init__(self, books=None):
        """
        Иницилизирует объект Library
        :param books: - список книг. По умолчанию будет пустой список
        """
        self.books = books or []
    def get_next_book_id(self):
        """
        Метод, который возвращающий идентификатор для добавления новой книги в библиотеку.

        Если книг в библиотеке нет, то возвращает 1.
        Если книги есть, то возвращает идентификатор последней книги увеличенный на 1.
        """
        if not self.books:
            return 1
        else:
            return max(book.id_ for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        """
        Метод, который возвращающает индекс книги в списке, который хранится в атрибуте экземпляра класса.

        Если книга существует, то возвращает индекс из списка.
        Если книги нет, то вызывает ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует".
        :param book_id: Идентификатор книги.
        """
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
