from bookstore_functions import *

def main():
    # Get users choice of action
    input_choice = input("Enter your choice:\n"
                        "'add' - Add a book\n"
                        "'update' - Update the stock quantity of a book\n"
                        "'display' - Display the details of a book\n"
                        "'generate' - Generate a report showing all books in the inventory\n"
                        "'calculate' - Calculate the total value of the current inventory\n"
                        "'identify' - Identify books with low stock\n"
                        "'remove' - Remove a book from the inventory\n"
                        "'quit' - Quit the program\n"
                        "Your choice: ")

    # Add a new book to inventory
    if input_choice == "add" or input_choice == "a":
        # Open books.csv file
        with open("books.csv", "r") as file:
            # Read books from CSV file
            books = file.readlines()
            # Remove newline characters
            books = [book.strip() for book in books]

            # Get new book
            new_book = input("Enter the details of the new book (id,title,author,price,quantity): ")

            # Use the add_book function to add the new book to the list of books
            books = add_book(books, new_book)

            # Print the updated list of books
            for book in books:
                print(book)

         # Open books.csv file in write mode
        with open("books.csv", "w") as file:
            # Write the updated list of books back to the CSV file
            for book in books:
                file.write(book + "\n")


    # Update the stock quantity of a book
    elif input_choice == "update" or input_choice == "u":
         with open("books.csv", "r") as file:
            # Read books from CSV file
            books = file.readlines()
            # Remove newline characters
            books = [book.strip() for book in books]

            # Get the book ID to update
            book_id = input("Enter the ID of the book to update: ")

            # Find the book with the given ID
            for i, book in enumerate(books):
                book_data = book.split(",")
                if book_data[0] == book_id:
                    # Get the new quantity from the user
                    new_quantity = input("Enter the new quantity for the book: ")
                    # Update the quantity of the book
                    book_data[4] = new_quantity
                    # Update the book in the list of books
                    books[i] = ",".join(book_data)
                    break

         with open("books.csv", "w") as file:
            # Write the updated list of books back to the CSV file
            for book in books:
                file.write(book + "\n")


    # Display a book from the inventory
    elif input_choice == "display" or input_choice == "d":
        with open("books.csv", "r") as file:
            # Read books from CSV file
            books = file.readlines()
            # Remove newline characters
            books = [book.strip() for book in books]

            # Get the book ID to display
            book_id = input("Enter the ID of the book to display: ")

            # Find the book with the given ID
            for book in books:
                book_data = book.split(",")
                if book_data[0] == book_id:
                    print(book_data)
                    break
    
    # Generate a report showing all books in the inventory
    elif input_choice == "generate" or input_choice == "g":
        with open("books.csv", "r") as file:
            # Read books from CSV file
            books = file.readlines()
            # Remove newline characters
            books = [book.strip() for book in books]

            # Use the generate_inventory_report function to generate the report
            report = generate_inventory_report(books)

            # Print the report with each book on a new line
            for book in report:
                print(book)

    # Calculate the total value of the current inventory
    elif input_choice == "calculate" or input_choice == "c":
        with open("books.csv", "r") as file:
            # Read books from CSV file
            books = file.readlines()

            # Skip the first line (headers)
            books = books[1:]

            # Remove newline characters and split each line into a list of values
            books = [book.strip().split(",") for book in books]

            # Convert each list of values into a dictionary
            books = [{"ID": book[0], "Title": book[1], "Author": book[2], "Quantity": float(book[3]), "Price": float(book[4])} for book in books]

            # Use the calculate_total_inventory_value function to calculate the total value
            total_value = calculate_total_inventory_value(books)

            # Print the total value
            print("Total value of current inventory: " + str(total_value))

    # Identify books with low stock
    elif input_choice == "identify" or input_choice == "i":
        threshold = int(input("Enter the threshold for low stock: "))
        with open("books.csv", "r") as file:
            # Read books from CSV file
            books = file.readlines()

            # Skip the first line (headers)
            books = books[1:]

            # Remove newline characters and split each line into a list of values
            books = [book.strip().split(",") for book in books]

            # Convert each list of values into a dictionary
            books = [{"ID": book[0], "Title": book[1], "Author": book[2], "Quantity": int(book[3]), "Price": float(book[4])} for book in books]

            # Use the identify_low_stock_books function to identify books with low stock
            low_stock_books = identify_low_stock_books(books, threshold)

            # Print the books with low stock
            print("Books with low stock:")
            for book in low_stock_books:
                print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Quantity: {book['Quantity']}, Price: {book['Price']}")

    
    # Remove a book from the inventory
    elif input_choice == "remove" or input_choice == "r":
        book_id = input("Enter the id of the book to remove: ")
        with open("books.csv", "r") as file:
            # Read books from CSV file
            books = file.readlines()

            # Remove newline characters and split each line into a list of values
            books = [book.strip().split(",") for book in books]

            # Convert each list of values into a dictionary
            books = [{"ID": book[0], "Title": book[1], "Author": book[2], "Quantity": book[3], "Price": book[4]} for book in books]

            # Use the remove_book function to remove the book with the given id
            books = remove_book(books, book_id)

            # Print the updated list of books
            for book in books:
                print(book)
            print("Successfully removed book with ID:", book_id)

        with open("books.csv", "w") as file:
            # Write the updated list of books back to the CSV file
            for book in books:
                book_string = f'{book["ID"]},{book["Title"]},{book["Author"]},{book["Quantity"]},{book["Price"]}\n'
                file.write(book_string)


    # Quit the program
    elif input_choice == "quit" or input_choice == "q":
        print("Goodbye!")
        return
    

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")

# Call the main function
if __name__ == "__main__":
    main()