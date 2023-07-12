class LibraryItem:
    def __init__(self, id, title, year):
        self.id = id
        self.title = title
        self.year = year

    def display_details(self):
        print(f"ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")


class Book(LibraryItem):
    def __init__(self, id, title, year, author):
        super().__init__(id, title, year)
        self.author = author

    def display_details(self):
        super().display_details()
        print(f"Author: {self.author}")


class Magazine(LibraryItem):
    def __init__(self, id, title, year, issue):
        super().__init__(id, title, year)
        self.issue = issue

    def display_details(self):
        super().display_details()
        print(f"Issue: {self.issue}")


book1 = Book(1, "The Great Gatsby", 1925, "F. Scott Fitzgerald")
book2 = Book(2, "To Kill a Mockingbird", 1960, "Harper Lee")
magazine1 = Magazine(3, "National Geographic", 2021, 12)
magazine2 = Magazine(4, "Time", 2022, 7)        


book1.display_details()
print()
book2.display_details()
print()
magazine1.display_details()
print()
magazine2.display_details()        