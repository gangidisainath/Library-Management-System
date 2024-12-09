# Library-Management-System with flask API
This project has 3 files.
1) main file Library_Management_flask.py
2) auth.py for authorization which contains the token.
3) data.py which stores books and members data.
# to run the project
run Library_Managemnt_System.py
/status helps to get status
/books 
GET request to get all books list and also to search books using title or author name.
POST request to add new book
/books/<book_id> to manage book data using it's id.
methods=[GET,POST,PUT]
/members 
methods=[GET,POST]
search books by title or author through endpoint /books
managebooks data by /books/<int:book_id> endpoint
****assumptions
   1)token for authorization is required for all crud operations on books and members.
   2)Input data is assumed to be properly formatted.
   3)assumed pagination for books as 5 per page.
   4)id of new book is given as per length of book list at that time.
****limitaions
   1)Data persists only while the application is running. Restarting the app resets the data
   2)Email addresses for members are stored as-is, with no validation for correct format or duplicates.
   3)The application is designed for local development.
