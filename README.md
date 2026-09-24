Invoice Generator

Invoice Generator is a simple Python project that creates a basic invoice for customers.

The program allows the user to enter multiple products, calculate item totals, and generate a final invoice with the total amount.

Features

- Enter customer name
- Add multiple products
- Enter product quantity
- Enter product price
- Calculate item total
- Calculate subtotal
- Display a formatted invoice
- Simple command-line interface
- No external libraries required

Technologies Used

- Python 3
- Lists
- Loops
- Functions and calculations
- User input
- Formatted output

Example

========================================
           INVOICE GENERATOR
========================================

Enter customer name: Ayush

Enter item name: Keyboard
Enter quantity: 1
Enter price: 800
Add another item? (y/n): y

Enter item name: Mouse
Enter quantity: 2
Enter price: 400
Add another item? (y/n): n

========================================
                INVOICE
========================================
Customer: Ayush
----------------------------------------
Item           Qty     Price     Total
----------------------------------------
Keyboard       1       800.00    800.00
Mouse          2       400.00    800.00
----------------------------------------
Subtotal:              ₹1600.00
Grand Total:           ₹1600.00
========================================
          Thank You For Shopping!
========================================

Project Structure

invoice-generator/
│
├── InvoiceGenerator.py
└── README.md

Requirements

- Python 3.x
- No external packages required

How to Run

Clone the repository:

git clone YOUR_REPOSITORY_URL

Open the project folder:

cd invoice-generator

Run the program:

python InvoiceGenerator.py

How It Works

1. Enter the customer's name.
2. Enter the product name.
3. Enter quantity and price.
4. The program calculates the item total.
5. Add more products if required.
6. The program calculates the subtotal.
7. A formatted invoice is displayed.

Learning Outcomes

This project helps practice:

- Python lists
- "while" loops
- "for" loops
- User input
- Arithmetic operations
- String formatting
- Formatted console output

Future Improvements

- Add GST calculation
- Add discount functionality
- Add invoice number
- Add date and time
- Save invoices as text files
- Generate PDF invoices
- Add customer contact details
- Add a graphical user interface

Project Type

Beginner Python Project

Author

Ayush Singh

BCA Student | Python Programmer | Learning DSA

License

This project is open source and available for learning and educational purposes.
