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


# TODO написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages
    def __str__(self):
        return  "Книга "+'"'+self.name+'"'
    def __repr__(self):
        return("Book(id_="+str(self.id_)+", name='"+self.name+"', pages="+str(self.pages)+')')
        pass

# TODO написать класс Library
class Library:
    def __init__(self, books = []):
        self.books = books
    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return (len(self.books)+1)
    def get_index_by_book_id(self, id):
        nakop = 0
        for i, b in enumerate(self.books):
            if b.id_ == id:
                nakop = 1
                return i
            if nakop == 0:
                raise ValueError('Книги с запрашиваемым id не существует')



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
