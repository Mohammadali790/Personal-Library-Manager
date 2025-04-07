import json

LIBRARY_FILE = "library.json"

def load_library():
    """Load the library data from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save the library data to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def get_valid_year(prompt):
    """Get a valid year from user input."""
    while True:
        try:
            year = int(input(prompt))
            if 0 < year <= 9999:
                return year
            else:
                print("Please enter a valid year (1–9999).")
        except ValueError:
            print("Invalid input. Please enter a numeric year.")

def get_yes_no(prompt):
    """Get a yes/no input from user."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["yes", "no"]:
            return answer == "yes"
        print("Please enter 'yes' or 'no'.")

def add_book(library):
    """Add a new book to the library."""
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = get_valid_year("Enter the publication year: ")
    genre = input("Enter the genre: ").strip().capitalize()
    read_status = get_yes_no("Have you read this book? (yes/no): ")

    # Check for duplicates
    for book in library:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            print("This book already exists in your library.")
            return

    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    })
    print("✅ Book added successfully!")

def remove_book(library):
    """Remove a book from the library by title."""
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found.")

def search_book(library):
    """Search for books by title or author."""
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice (1/2): ").strip()
    query = input("Enter search query: ").strip().lower()

    results = [
        book for book in library 
        if query in book["title"].lower() or query in book["author"].lower()
    ]

    if results:
        print("\n📚 Matching Books:")
        for i, book in enumerate(results, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

def display_books(library):
    """Display all books in the library."""
    if not library:
        print("📂 Your library is empty.")
        return

    print("\n📚 Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    """Display reading statistics and genre breakdown."""
    total = len(library)
    if total == 0:
        print("No books in the library.")
        return

    read_count = sum(book["read"] for book in library)
    unread_count = total - read_count
    percentage_read = (read_count / total) * 100

    print("\n📊 Library Statistics:")
    print(f"Total books     : {total}")
    print(f"Books read      : {read_count}")
    print(f"Books unread    : {unread_count}")
    print(f"Read percentage : {percentage_read:.2f}%")

    # Genre summary
    genre_count = {}
    for book in library:
        genre = book["genre"]
        genre_count[genre] = genre_count.get(genre, 0) + 1

    print("\n📘 Genre Distribution:")
    for genre, count in genre_count.items():
        print(f"- {genre}: {count} book(s)")

def main():
    """Main loop of the Library Manager."""
    library = load_library()

    while True:
        print("\n" + "="*40)
        print("📖 Welcome to Personal Library Manager 📖")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        print("="*40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("💾 Library saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
