books = []

while True:
    print("\n📚 Library Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("✅ Book added successfully!")

    elif choice == "2":
        if not books:
            print("No books available.")
        else:
            print("\n📖 Available Books:")
            for i, book in enumerate(books, start=1):
                print(f"{i}. {book}")

    elif choice == "3":
        book = input("Enter book name to issue: ")

        if book in books:
            books.remove(book)
            print(f"📕 '{book}' has been issued.")
        else:
            print("❌ Book not available.")

    elif choice == "4":
        book = input("Enter book name to return: ")
        books.append(book)
        print(f"📗 '{book}' has been returned.")

    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
