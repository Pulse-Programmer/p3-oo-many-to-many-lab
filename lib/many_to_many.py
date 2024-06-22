class Author:
    all = []
    def __init__(self, name: str) -> None:
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

class Book:
    all = []
    def __init__(self, title:str) -> None:
        self.title = title
        Book.all.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []
    def __init__(self, author: Author, book: Book, date: str, royalties: int) -> None:
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self) -> Author:
        return self._author

    @author.setter
    def author(self, author) -> None:
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception

    @property
    def book(self) -> Book:
        return self._book

    @book.setter
    def book(self, book) -> None:
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception
        
    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, date) -> None:
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception

    @property
    def royalties(self) -> int:
        return self._royalties

    @royalties.setter
    def royalties(self, royalties) -> None:
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception
        
    @classmethod
    def contracts_by_date(cls, date):
        '''should return all contracts that have the same date as the date passed into the method'''
        return [contract for contract in cls.all if contract.date == date]