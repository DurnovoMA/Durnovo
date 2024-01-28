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

    def __str__(self) -> str:
        """
        Метод возвращает строку формата:  Книга "название_книги"
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Метод возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр.
        """
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
