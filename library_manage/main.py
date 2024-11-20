import json
class Book:
    def __init__(self, title, author, description, s_number):
        self.title = title
        self.author = author
        self.ability = True
        self.description = description
        self.serial_number = s_number

    def display_details(self):
        return print(f"Book Name: {self.title}, Book Author: {self.author}, Book Details: {self.description}, Book Serial Number: {self.serial_number}")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = {}

    def add_borrowed_book(self, book):
        self.borrowed_books[book.serial_number] = book
        print(f"Book '{book.title}' added to {self.name}'s borrowed books.")

    def display_details(self):
        books = ', '.join(book.title for book in self.borrowed_books.values())
        print(f"Member Name: {self.name}, User ID: {self.member_id}, Borrowed Books: {books if books else 'None'}")


class LibraryManagementSystem:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author, description, s_number):
        if s_number in self.books:
            print("Book already exists.")
        else:
            book = Book(title, author, description, s_number)
            self.books[s_number] = book
            print("Book added successfully.")

    def add_member(self, name, member_id):
        if member_id in self.members:
            print("Member already exists.")
        else:
            member = Member(name, member_id)
            self.members[member_id] = member
            print("Member added successfully.")

    def borrow_book(self, member_id, s_number):
        member = self.members.get(member_id)
        book = self.books.get(s_number)
        if not member:
            print(f"No member found with ID {member_id}.")
            return
        if not book:
            print(f"No book found with serial number {s_number}.")
            return
        if not book.ability:
            print(f"Book '{book.title}' is already borrowed.")
            return

        member.add_borrowed_book(book)
        book.ability = False
        print(f"Book '{book.title}' borrowed successfully by {member.name}.")

    def display_books(self):
        for book in self.books.values():
            book.display_details()

    def display_members(self):
        for member in self.members.values():
            member.display_details()

    def return_book(self, member, book):
        pass

    def display_all_books(self):
        pass

    def search_book(self, serial_number):
        pass

    def remove_book(self, serial_number):
        pass


def display_menu():
    pass


def main():
    library = LibraryManagementSystem()

    # Adding some initial books and members
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_member("Alice")
    library.add_member("Bob")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. View Available Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View Borrowed Books")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            library.add_book(title, author)

        elif choice == '2':
            name = input("Enter member name: ")
            library.add_member(name)

        elif choice == '3':
            library.list_available_books()

        elif choice == '4':
            member_name = input("Enter member name: ")
            book_title = input("Enter book title to borrow: ")
            library.lend_book(member_name, book_title)

        elif choice == '5':
            member_name = input("Enter member name: ")
            book_title = input("Enter book title to return: ")
            library.return_book(member_name, book_title)

        elif choice == '6':
            member_name = input("Enter member name: ")
            member = library._find_member(member_name)
            if member:
                member.list_borrowed_books()

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()