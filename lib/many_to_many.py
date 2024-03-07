class Book:
    # Class variable
    all_books = []

    # Constructor
    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

class Author:
    # Class variable
    all_authors = []

    # Constructor
    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    # Method to retrieve contracts associated with the author
    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    # Method to retrieve unique books associated with the author
    def books(self):
        unique_books = []
        for contract in self.contracts:
            book = contract.book
            if book not in unique_books:
                unique_books.append(book)
        return unique_books

    # Method to sign a new contract for the author
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    # Method to calculate total royalties earned by the author
    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total

class Contract:
    # Class variable
    all_contracts = []

    # Constructor
    def __init__(self, author, book, date, royalties):
        # Check if the arguments are of the correct types
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int) and not isinstance(royalties, float):
            raise Exception("Royalties must be a number.")
        if royalties < 0 or royalties > 100:  # Check if royalties are within the range
            raise Exception("Royalties must be between 0 and 100.")  # Raise exception if royalties are out of range

        # Assign properties
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    # Class method to retrieve contracts by date
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]