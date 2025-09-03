

j={}
def save_library_to_txt(serial, book):
    if not is_in_file(serial, book.books):
        with open("library_data.txt", "a") as f:
            f.write(f"Serial No {serial}: {book}\n")


def start():
    print("welcome to bhvy's library")
    v=input("do you wanna add books to the library?")
    if v=="yes":
        lib()
    else:
        whattodo()
def lib():
    a=int(input("serialno of the books: "))
    b=input("name of the book: ")


    
    class library:
        def __init__(self,a,b):
            self.no_of_books=a
            self.books=b    
        
        def __str__(self):
            return f"SerialNo of books: {self.no_of_books}, Name of books: {self.books}"
        
        def __repr__(self):
            return self.__str__()
        
            
    j[a]=library(a, b)
    save_library_to_txt(a,j[a])
    asking()
def asking():
    l=input("do you wanna see the database of the books? (P.S. TYPE add TO ADD MORE BOOKS and TYPE show to show all library things) ")
    if l=="yes":
       show_saved_books()
       
    elif l=="add":
        lib()
        
    else:
        print("tata byebye")
        
        


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
    g=input("do you want to see the books present in the library?: ")
    if g=="yes":
        show_saved_books()
    else:
        print("bruh then go away, why u here")
        exit()


def is_in_file(serial, name):
    try:
        with open("library_data.txt", "r") as f:
            for line in f:
                if f"Serial No {serial}:" in line or name in line:
                    return True
    except FileNotFoundError:
        return False
    return False






start()
