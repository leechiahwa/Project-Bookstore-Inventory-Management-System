# Add a new book to inventory
def add_book(books, new_book):
    books.append(new_book)
    return books


# Update the stock quantity of a book
def update_quantity(books, book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


# Display the details of a specific book
def display_book_details(books, book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


# Generate a report showing all books in the inventory
def generate_inventory_report(books):
    return books


# Calculate the total value of the current inventory
def calculate_total_inventory_value(books):
    total_value = 0
    for book in books:
        total_value += book["quantity"] * book["price"]
    return total_value


# Identify books with low stock (quantity below a certain threshold)
def identify_low_stock_books(books, threshold):
    low_stock_books = []
    for book in books:
        if book["quantity"] < threshold:
            low_stock_books.append(book)
    return low_stock_books
    

# Remove a book from the inventory
def remove_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            break
    return books
