from bookstore_functions import *

def main():
    # Get users choice of action
    input_choice = input("\nEnter your choice:\n"
                        "'a' - Add a book\n"
                        "'u' - Update the stock quantity of a book\n"
                        "'d' - Display the details of a book\n"
                        "'g' - Generate a report showing all books in the inventory\n"
                        "'c' - Calculate the total value of the current inventory\n"
                        "'i' - Identify books with low stock\n"
                        "'r' - Remove a book from the inventory\n"
                        "'q' - Quit the program\n"
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
            # new_book = input("Enter the details of the new book (id,title,author,quantity,price): ")
            # Generate a unique ID for the new book
            new_id = input("Enter the ID of the new book: ")
            # Check for duplicate ID
            for book in books:
                book_data = book.split(",")
                if book_data[0] == new_id:
                    print("Error: Book with ID", new_id, "already exists.")
                    main()
                    return 
                
            # Get the details of the new book from the user
            new_title = input("Enter the title of the new book: ")
            new_author = input("Enter the author of the new book: ")
            new_quantity = input("Enter the quantity of the new book: ")
            new_price = input("Enter the price of the new book: ")

            # Create a string representation of the new book
            new_book = f"{new_id},{new_title},{new_author},{new_quantity},{new_price}"

            # Use the add_book function to add the new book to the list of books
            books = add_book(books, new_book)

            # Print the updated list of books
            print("New book added: " + new_book)

         # Open books.csv file in write mode
        with open("books.csv", "w") as file:
            # Write the updated list of books back to the CSV file
            for book in books:
                file.write(book + "\n")

        # Call the main function again to allow the user to make another choice
        main()            


    # Update the stock quantity of a book
    elif input_choice == "update" or input_choice == "u":
        with open("books.csv", "r") as file:
            # Read books from CSV file
            books = file.readlines()
            # Remove newline characters
            books = [book.strip() for book in books]

            # Get the book ID to update
            book_id = input("Enter the ID of the book to update: ")
            # Check if the book ID is available in the inventory
            book_ids = [book.split(",")[0] for book in books]
            if book_id not in book_ids:
                print("Error: Book with ID", book_id, "does not exist.")
                main()
                return

            # Find the book with the given ID
            for i, book in enumerate(books):
                book_data = book.split(",")
                if book_data[0] == book_id:
                    # Get the new quantity as an integer from the user
                    while True:
                        try:
                            new_quantity = int(input("Enter the new quantity for the book: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter an integer.")
                    # Update the quantity of the book
                    book_data[3] = str(new_quantity)
                    # Update the book in the list of books
                    books[i] = ",".join(book_data)

                    # Print a message to show the quantity was updated successfully 
                    print("Quantity updated!")
                    print("Book ID:", book_data[0])
                    print("Updated quantity:", new_quantity)
                    break

        with open("books.csv", "w") as file:
            # Write the updated list of books back to the CSV file
            for book in books:
                file.write(book + "\n")

        # Call the main function again to allow the user to make another choice
        main()
        

    # Display a book from the inventory
    elif input_choice == "display" or input_choice == "d":
        with open("books.csv", "r") as file:
            # Read books from CSV file
            books = file.readlines()
            # Remove newline characters
            books = [book.strip() for book in books]

            # Get the book ID to display
            while True:
                book_id = input("Enter the ID of the book to display: ")
                book_ids = [book.split(",")[0] for book in books]
                if book_id in book_ids:
                    break
                else:
                    print("Error: Book with ID", book_id, "does not exist.")

            # Find the book with the given ID
            for book in books:
                book_data = book.split(",")
                if book_data[0] == book_id:
                    print(book_data)
                    break
            
        # Call the main function again to allow the user to make another choice
        main()
    
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

        # Call the main function again to allow the user to make another choice
        main()

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
            books = [{"ID": book[0], "Title": book[1], "Author": book[2], "quantity": float(book[3]), "price": float(book[4])} for book in books]

            # Use the calculate_total_inventory_value function to calculate the total value
            total_value = calculate_total_inventory_value(books)

            # Print the total value
            print("Total value of current inventory: RM" + str(total_value))

        # Call the main function again to allow the user to make another choice
        main()

    # Identify books with low stock
    elif input_choice == "identify" or input_choice == "i":
        # Get the threshold for low stock from the user
        while True:
            threshold_input = input("Enter the threshold for low stock: ")
            if threshold_input.isdigit():
                threshold = int(threshold_input)
                break
            else:
                print("Invalid input. Please enter a number.")
                
        with open("books.csv", "r") as file:
            # Read books from CSV file
            books = file.readlines()

            # Skip the first line (headers)
            books = books[1:]

            # Remove newline characters and split each line into a list of values
            books = [book.strip().split(",") for book in books]

            # Convert each list of values into a dictionary
            books = [{"ID": book[0], "Title": book[1], "Author": book[2], "quantity": int(book[3]), "price": float(book[4])} for book in books]

            # Use the identify_low_stock_books function to identify books with low stock
            low_stock_books = identify_low_stock_books(books, threshold)

            # Print the books with low stock
            print("Books with low stock:")
            for book in low_stock_books:
                print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Quantity: {book['quantity']}, Price: {book['price']}")
            
        # Call the main function again to allow the user to make another choice
        main()

    
    # Remove a book from the inventory
    elif input_choice == "remove" or input_choice == "r":
        while True:
            book_id = input("Enter the id of the book to remove: ")
            
            with open("books.csv", "r") as file:
                # Read books from CSV file
                books = file.readlines()

                # Remove newline characters and split each line into a list of values
                books = [book.strip().split(",") for book in books]

                # Convert each list of values into a dictionary
                books = [{"id": book[0], "Title": book[1], "Author": book[2], "Quantity": book[3], "Price": book[4]} for book in books]

                # Check if the book with the given id exists
                book_ids = [book["id"] for book in books]
                if book_id in book_ids:
                    break
                else:
                    print("Error: Book with ID", book_id, "does not exist.")

        # Use the remove_book function to remove the book with the given id
        books = remove_book(books, book_id)
        # Print a message to show the book was removed successfully
        print("Successfully removed book with ID:", book_id)

        with open("books.csv", "w") as file:
            # Write the updated list of books back to the CSV file
            for book in books:
                book_string = f'{book["id"]},{book["Title"]},{book["Author"]},{book["Quantity"]},{book["Price"]}\n'
                file.write(book_string)

        # Call the main function again to allow the user to make another choice
        main()
        

    # Quit the program
    elif input_choice == "quit" or input_choice == "q":
        print("Goodbye!")
        return
    

    # Invalid choice
    else:
        print("Invalid choice. Please try again.\n")
        
        # Call the main function again to allow the user to make another choice
        main()
    
# Call the main function
if __name__ == "__main__":
    main()
