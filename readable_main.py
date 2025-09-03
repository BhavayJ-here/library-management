j = {}

class Library:
    def __init__(self, serial, name):
        self.no_of_books = serial
        self.books = name

    def __str__(self):
        return f"SerialNo of books: {self.no_of_books}, Name of books: {self.books}"

    def __repr__(self):
        return self.__str__()


def save_library_to_txt(serial, book):
    if not is_in_file(serial, book.books):
        with open("library_data.txt", "a") as f:
            f.write(f"Serial No {serial}: {book}\n")


def is_in_file(serial, name):
    try:
        with open("library_data.txt", "r") as f:
            for line in f:
                if f"Serial No {serial}:" in line or name in line:
                    return True
    except FileNotFoundError:
        return False
    return False


def start():
    print("Welcome to bhvy's library")
    v = input("Do you wanna add books to the library? ")
    if v.lower() == "yes":
        lib()
    else:
        whattodo()


def lib():
    a = int(input("Serial no of the books: "))
    b = input("Name of the book: ")

    j[a] = Library(a, b)
    save_library_to_txt(a, j[a])
    asking()


def asking():
    l = input("Do you wanna see the database of the books? (P.S. TYPE add TO ADD MORE BOOKS and TYPE show to show all library things) ")
    if l.lower() == "yes" or l.lower() == "show":
        show_saved_books()
    elif l.lower() == "add":
        lib()
    else:
        print("Tata byebye")


def show_saved_books():
    try:
        with open("library_data.txt", "r") as f:
            content = f.read()
            if content.strip():
                print(content)
            else:
                print("No books in the saved library.")
    except FileNotFoundError:
        print("No saved library found.")


def whattodo():
    g = input("Do you want to see the books present in the library? ")
    if g.lower() == "yes":
        show_saved_books()
    else:
        print("Bruh then go away, why you here?")
        exit()


start()
