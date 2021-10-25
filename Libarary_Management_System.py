class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayBooks(self):
        print("\nAvailable books for now: ")
        for books in self.books:
            print(" *" + books)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"The book {bookName} is available at this moment with only 1 copy and it is successfully issued by you. Make sure to return it within 30 days\n"
            )
            self.books.remove(bookName)
            return bookName

        else:
            print(f"The book {bookName} is not available right now")

    def returnBook(self, bookName):
        if bookName in self.books:
            print("There is no book in your record to return")
        else:
            self.books.append(bookName)
            print(f"Thanks for returning our {bookName} book")


class Student:
    def requestBook(self):
        book = input("Enter the name of the book which you want to borrow: ")
        self.book = book.upper()
        return self.book

    def withdrawBook(self):
        return self.book


def Show_Menu():
    print("Menu")
    print("1. Show all the books")
    print("2. Request a book")
    print("3. Return the book")
    print("4. Quit")


if __name__ == "__main__":
    welcomeMessage = "WELCOME TO KOLKATA NATIONAL DIGITAL LIBRARY\n"
    print(welcomeMessage)

    centralLibrary = Library(
        [
            "MCU COMICS",
            "ALGORITHMS",
            "JAVA",
            "ESSENTIALS OF PYTHON",
            "JEE STUDY MATERIALS",
            "HC VERMA PHYSICS"
        ]
    )
    Partha = Student()

    global borrwedBook

    while True:
        Show_Menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            centralLibrary.displayBooks()

        elif choice == 2:
            requestedBook = Partha.requestBook()
            borrwedBook = centralLibrary.borrowBook(requestedBook)

        elif choice == 3:
            print(f"Your borrowed book: {borrwedBook}")
            if requestedBook == borrwedBook:
                centralLibrary.returnBook(Partha.withdrawBook())
            else:
                print(
                    "As you dont have any borrowed book. So you cannot return anything.Sorry\n"
                )

        elif choice == 4:
            print("Thanks for visiting our digital library. Have a safe day")
            quit()

        else:
            print("\nEnter only options given below")