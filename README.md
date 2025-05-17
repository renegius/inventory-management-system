# Inventory Management System

A desktop inventory management application built in Python using Tkinter and MySQL.

## Features

- Full CRUD operations (Create, Read, Update, Delete)
- GUI interface using Tkinter and ttk.Treeview
- Integration with MySQL database (pymysql)
- Dynamic data table with search, selection, and filters
- Error handling and form validation
- Modular code structure for maintainability

## Technologies

- Python
- Tkinter
- MySQL
- pymysql

## Setup Instructions

1. Install Python 3 and MySQL on your machine.
2. Clone this repository or download the source files.
3. Create a MySQL database named `stockmanagementsystem` and a table `stocks` with appropriate columns:
    ```sql
    CREATE DATABASE stockmanagementsystem;

    USE stockmanagementsystem;

    CREATE TABLE stocks (
        item_id INT AUTO_INCREMENT PRIMARY KEY,
        item_name VARCHAR(100),
        item_price DECIMAL(10, 2),
        item_qnty INT,
        item_category VARCHAR(100),
        item_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```
4. Update the database connection details in the script (host, user, password).
5. Run the script using:
    ```bash
    python inventory_management.py
    ```

## Screenshots

_Add screenshots of the application interface here if available._

## Author

Anthony Cepeda
