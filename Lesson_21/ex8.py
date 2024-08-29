#Create a dictionary of book titles and their authors. Write a function to search for a book by its title and return the author's name.

books = {
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "The Great Gatsby": "F. Scott Fitzgerald",
}

def find_author_by_title(title):
    author = books.get(title)
    if author:
        return author
    else:
        return "Book not found."

book_title = "1984"
print(f"The author of '{book_title}' is {find_author_by_title(book_title)}")
