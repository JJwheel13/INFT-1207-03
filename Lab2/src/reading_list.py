import csv

BOOKS_FILE = 'books.csv'


# Utility function to read all books from the CSV file
def read_books():
    try:
        with open(BOOKS_FILE, mode='r', newline='') as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist


# Utility function to write all books back to the CSV file
def write_books(books):
    try:
        with open(BOOKS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(books)
        return True
    except IOError:
        print("Error writing to the file.")
        return False


# Function to add a book to the reading list
def add_book(title, author, year):
    if not title or not author or not year:
        print("Error: All fields are required.")
        return False

    if not year.isdigit() or int(year) < 0:
        print("Error: Invalid year. Please enter a valid positive number.")
        return False

    try:
        with open(BOOKS_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, author, year])
        print(f'Book "{title}" added successfully.')
        return True
    except IOError:
        print("Error writing to the file.")
        return False


# Function to list all books
def list_books():
    books = read_books()

    if not books:
        print("No books found.")
        return False

    print("\nBook List:")
    for row in books:
        print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
    return True


# Function to search for a book by title
def search_book(title):
    books = read_books()

    for row in books:
        if row[0].strip().lower() == title.strip().lower():
            print(f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
            return True
    print('Book not found.')
    return False


# Function to delete a book by title
def delete_book(title):
    books = read_books()

    updated_books = [row for row in books if row[0].strip().lower() != title.strip().lower()]

    if len(updated_books) == len(books):
        print("Book not found.")
        return False
    else:
        write_books(updated_books)
        print(f'Book "{title}" deleted successfully.')
        return True


# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Book\n5. Quit")
        choice = input("Select an option: ").strip()

        if choice == '1':
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            year = input("Enter year of publication: ").strip()
            add_book(title, author, year)
        elif choice == '2':
            list_books()
        elif choice == '3':
            title = input("Enter book title to search: ").strip().lower()
            search_book(title)
        elif choice == '4':
            title = input("Enter book title to delete: ").strip().lower()
            delete_book(title)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    menu()
