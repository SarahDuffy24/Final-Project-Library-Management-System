For my project, I built a Library Management System using Python to manage books in a library. The system stores book details—
like the book ID, title, author,  category, and availability status—in a CSV file. 
I started by writing functions to load the books from the CSV file and save any updates back to it. Then, I created features to add, 
update, and remove books from the library. When adding a new book, 
I made sure that each book has a unique ID, and for updates,
 I let users modify details like the title, author, and category. For checking out and returning books, 
 I included a status system that changes the book’s status between "available" and "issued" based on whether it's checked out or not. 
 I also built a search feature so users could easily find books by title, author, category, or status
  The main part of the program is a simple menu that gives users a list of options like adding books, searching, or viewing all books. 
  Users can keep interacting with the system until they choose to exit, at which point the program saves all changes to the CSV file.

While the project was overall rewarding, I did face some difficulties 
One challenge was ensuring that all the book data was properly loaded from the CSV file and then saved correctly after any changes. 
I struggled with reading and writing the data back in the right format without losing any information, 
 I also found it tricky to manage user input and 
ensure that the system was flexible enough to handle unexpected or incorrect input. For example, when updating book details,
I had to make sure users could leave fields blank if they didn’t want to change certain details,
Another challenge i faced was implementing the checkout and return functionality.