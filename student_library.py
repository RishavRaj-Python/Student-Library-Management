class Library:
    def __init__(self, book_list):
        self.books = book_list

    def display_books(self):
        print("\nAvailable Books in the Library:")
        if len(self.books) == 0:
            print("No books available right now.")
        else:
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"You have borrowed '{book_name}'.")
            return True
        else:
            print("This book is not available.")
            return False

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"Thanks for returning '{book_name}'.")


class Student:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def request_book(self):
        return input("Enter the name of the book you want to borrow: ")

    def return_book(self):
        return input("Enter the name of the book you want to return: ")


if __name__ == "__main__":
    library = Library([
        "Python Programming",
        "Data Structures",
        "Machine Learning",
        "Artificial Intelligence",
        "Database Management System"
    ])

    student = Student("Rishav")

    while True:
        print("\n====== Student Library Menu ======")
        print("1. Display all available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            library.display_books()

        elif choice == '2':
            req_book = student.request_book()
            if library.borrow_book(req_book):
                student.borrowed_books.append(req_book)

        elif choice == '3':
            ret_book = student.return_book()
            if ret_book in student.borrowed_books:
                library.return_book(ret_book)
                student.borrowed_books.remove(ret_book)
            else:
                print("You cannot return a book you haven't borrowed!")

        elif choice == '4':
            print("Thanks for using the Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter between 1-4.")
