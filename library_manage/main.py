import json
class Book:
    def __init__(self, title, author, description, s_number):
        self.title = title
        self.author = author
        self.ability = True
        self.description = description
        self.serial_number = s_number

    def display_book_details(self):
        return print(f"Book Name: {self.title}, Book Author: {self.author}, Book Details: {self.description}, Book Serial Number: {self.serial_number}")

    def return_book(self):
        self.ability = True

class Member():
    def __init__(self, name, member_id, mex_book=0):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = {}
        self.mex_book = mex_book

    def add_borrowed_book(self, book):
        self.borrowed_books[book.serial_number] = book
        print(f"Book '{book.title}' added to {self.name}' borrowed books.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.serial_number)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"You have not borrowed {book.title}.")

    def display_member_details(self):
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

    def list_available_books(self):
        for book in self.books.values():
            book.display_book_details()

    def display_members(self):
        for member in self.members.values():
            member.display_member_details()

    def return_book(self, member_id, s_number):
        member = self.members.get(member_id)
        book = self.books.get(s_number)
        if member and book:
            member.return_book(book)
        else:
            print("Invalid member ID or book serial number.")




def main():
    library = LibraryManagementSystem()

    # Adding some initial books and members
    library.add_book("To Kill a Mockingbird","Harper Lee", "George Orwell","1984")
    library.add_book("Ritch Dad Poor Dad", "Albard Jonson", "About","1990" )
    library.add_member("Alice", "A2006")
    library.add_member("Bob","B2006")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. View Available Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Display All Member")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            description = input("Enter the book description: ")
            s_number = input("Enter the book serial number: ")
            library.add_book(title, author,description, s_number)

        elif choice == '2':
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.add_member(name, member_id)

        elif choice == '3':
            library.list_available_books()

        elif choice == '4':
            member_id = input("Enter member ID: ")
            s_number = input("Enter book serial number: ")
            library.borrow_book(member_id, s_number)

        elif choice == '5':
            member_id = input("Enter member ID: ")
            s_number = input("Enter book serial number: ")
            library.return_book(member_id, s_number)

        elif choice == '6':
            library.display_members()

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()