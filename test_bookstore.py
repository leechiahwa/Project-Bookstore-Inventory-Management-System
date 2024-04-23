import unittest
from bookstore_functions import *

class TestBookstoreFunctions(unittest.TestCase):
    def setUp(self):
        # Sample inventory for testing with consistent lowercase key names
        self.books = [
            {"id": 1, "title": "Introduction to Python", "author": "John Smith", "quantity": 50, "price": 29.99},
            {"id": 2, "title": "Data Science Essentials", "author": "Jane Doe", "quantity": 30, "price": 39.99},
            {"id": 3, "title": "Algorithm Design", "author": "Bob Johnson", "quantity": 20, "price": 49.99}
        ]

    def test_add_book(self):
        new_book = {"id": 21, "title": "Book 4", "quantity": 20, "price": 30}
        updated_inventory = add_book(self.books, new_book)
        self.assertIn(new_book, updated_inventory)

    def test_update_quantity(self):
        updated_book = update_quantity(self.books, 2)
        self.assertEqual(updated_book["id"], 2)
        self.assertEqual(updated_book["quantity"], 30)  # Assuming no actual update in the function

    def test_display_book_details(self):
        book_details = display_book_details(self.books, 3)
        self.assertEqual(book_details["id"], 3)
        self.assertEqual(book_details["title"], "Algorithm Design")

    def test_generate_inventory_report(self):
        inventory_report = generate_inventory_report(self.books)
        self.assertEqual(len(inventory_report), 3)

    def test_calculate_total_inventory_value(self):
        total_value = calculate_total_inventory_value(self.books)
        self.assertEqual(total_value, (50 * 29.99) + (30 * 39.99) + (20 * 49.99))

    def test_identify_low_stock_books(self):
        low_stock = identify_low_stock_books(self.books, 10)
        self.assertEqual(len(low_stock), 0)  # No books below quantity 10

    def test_remove_book(self):
        updated_inventory = remove_book(self.books, 1)
        self.assertNotIn({"id": 1, "title": "Introduction to Python", "quantity": 50, "price": 29.99}, updated_inventory)


if __name__ == '__main__':
    unittest.main()