import csv



def load_books(filename):
    "read the books from csv file and create a list of books"
    books = []
    with open(filename, 'r' , newline='', encoding ='utf-8')as f:
        reader = csv.DictReader(f)
        for row in reader:
#loop through each book in CSV File
            book = {
                'bid': row.get('bid' , '').strip (),
                'title': row.get('title', '').strip(),
                'author': row.get('author', '').strip(),
                'category': row.get('category', '').strip(),
                'status': row.get('status', '').strip(),
            }
                #Only add if 'bid' is not empty to avoid blank rows
            if book['bid']:
                book.append(book)
    return books

def save_books(filename, books):
    #Saves the list of books to a CSV file
    fieldnames = ['bid' , 'title' , 'author', 'category' , 'status']
    with open(filename, 'w', newline='', encoding= 'utf-8' ) as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            writer.writerow(book)

def add_book(books, bid, title, author, category):
    #adding new book to library , bid is not already taken
    for b in books: 
        if b['bid']== bid:
            print(f"Book '{title}' added.")
            return
    book = {'bid': bid, 'title': title, 'author':author, 'category': category, 'status': 'available'}
    books.append(book)
    print(f"Book '{title}' added. ")

    def update_book(books, bid):
        # updates the details of an existing book by ID
        for book in books:
            if book['bid'] == bid:
                new_title = input("Enter a new title(leave blank to keep current): ").strip()
                new_author = input("Enter a new author(leave blank to keep current): ").strip()
                new_category = input("Enter a new category(leave blank to keep current): ").strip()

                if new_title:
                    book['title'] = new_title
                if new_author:
                    book['author'] = new_author
                if new_category:
                    book['category'] = new_category

                print("Book updated")
                return
        print("Book not found.")

def remove_book(books, bid):
    for i, book in enumerate(books):
        if book['bid'] == bid:
            del books[i]
            print(f"Book with ID '{bid}' removed. ")
            return
    print("book not found. ")


    def checkout_book(books, bid):
        # check out a book from the library by ID" 
        for book in books:
            if book['status'] == 'available':
                book['status'] = 'issued'
                print(f"Book '{book['title']}' (ID: {bid}) checked out. ")
            else:
                print(f"Book '{book['title']}' (ID: {bid}) is already checked out. ")
            return
        print("Book not found")


def return_book(books, bid):
    for book in books:
        if book['bid'] == bid:
            if book['status'] == 'issued' :
                book['status'] = 'available'
                print(f"Book '{book['title']}' (ID: {bid}) returned. ")
            else:
                print(f"Book '{book['title']}' (ID: {bid}) was not checked out. ")
                return
    print("Book not found")


def search_book(books, search_type, keyword):
#searches for books by title, author, category, or status.""
    results = []
    keyword = keyword.lower()
    for book in books:
        if search_type == 'title' and keyword in book['title'].lower():
            results.append(book)
        elif search_type == 'author' and keyword in book['author'].lower():
            results.append(book)
        elif search_type == 'category' and keyword in book['category'].lower():
            results.append(book)
        elif search_type == 'status' and keyword in book['status'].lower():
            results.append(book)
    return results

def list_books(books):
    #Lists all books in library
    if not books:
        print("No books in the library")
    else:
        for book in books:
            print(f"ID: {book['bid']}, Title: {book['title']}, Author: {book['author']}, Category: {book['category']}, Status: {book['status']}")




