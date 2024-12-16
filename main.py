import library

def main():
    file_name = "Books_Data.csv"
    books = library.load_books(file_name)

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Remove Book")
        print("4. Check out Book")
        print("5. Return Book")
        print("6. Search Book")
        print("7. List All Book")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            bid = input("Enter book ID: ").strip()
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            category = input("Enter category: ").strip()
            if bid and title and category:
                library.add_book(books, bid, title, author, category)
            else:
                print(" All field (ID, title, author, category) are required. ")

        elif choice == '2':
            bid = input("Enter the book ID to update: ").strip()
            if bid:
                library.update_book(books, bid)
            else: 
                print("Book ID is required")

        elif choice == '3':
            bid = input("Enter the book ID to remove: ").strip()
            if bid:
                library.remove_book(books, bid)
            else: 
                print("Book ID is required")

        elif choice == '4':
            bid = input("Enter the book ID to check out: ").strip()
            if bid:
                library.checkout_book(books, bid)
            else: 
                print("Book ID is required")

        elif choice == '5':
            bid = input("Enter the book ID to return: ").strip()
            if bid:
                library.return_book(books, bid)
            else: 
                print("Book ID is required")

        elif choice == '6':
            print("Search by:")
            print("a. Title:")
            print("b. Author")
            print("c. Category")
            print("d. status(avaialble/checked out)")
            option = input(" Enter your choice (a-d): ").strip().lower()

            if option == 'a':
                keyword = input("Enter title keyword: ").strip()
                results = library.search_books(books, 'title' , keyword)
            elif option == 'b':
                keyword = input("Enter author name: ").strip()
                results = library.search_books(books, 'author' , keyword)
            elif option == 'c':
                keyword = input("Enter category: ").strip()
                results = library.search_books(books, 'category' , keyword)
            elif option == 'd':
                keyword = input("Enter (status(avaialble/checked out): ").strip()
                results = library.search_books(books, 'status' , keyword)
            else:
                print("Invalid option.")
                continue


            if results:
                for book in results:
                    print(f"ID: {book['bid']}, Title: {book['title']},  Author: {book['author']}, Category: {book['category']}, Status: {book['status']}")
            else:
               ("No books found") 

        elif choice == '7':
            library.list_books(books)

        elif choice == '8':
            library.save_books(file_name, books)
            print("Library data saved. GOODBYE!")
            break
        else:print("Invalid choice. Please try again. ")

main()

        





                                                                    




            



            





