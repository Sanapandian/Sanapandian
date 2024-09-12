Medical Store Management System
Overview
This project is a Medical Store Management System implemented in Python with MySQL as the database backend. It provides functionality to manage medicines in a medical store, including adding, viewing, updating, and deleting records. The system is console-based and allows users to interact with the database through a simple text menu.

Features
Add Medicine: Insert new medicine records into the database.
View Medicines: Display all medicines stored in the database.
Update Medicine: Modify existing medicine records based on their ID.
Delete Medicine: Remove medicine records from the database.
Prerequisites
Python 3.x
MySQL Server
pymysql library
Setup
Clone the Repository:
git clone https://github.com/yourusername/medical-store-management-system.git
cd medical-store-management-system
Install Dependencies: Ensure you have pymysql installed. You can install it using pip:
pip install pymysql
Set Up the Database:

Create a new database in MySQL named medicalstore.
Create the medicines table using the following SQL command:

CREATE TABLE medicines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE,
    category VARCHAR(100),
    price DECIMAL(10,2),
    quantity INT,
    manufacturer_name VARCHAR(100),
    expdate DATE
);
Configure Database Connection:

Open the main.py file.
Update the connect_to_db function with your MySQL credentials if necessary:

def connect_to_db():
    return pymysql.connect(host="localhost", user="yourusername", password="yourpassword", db="medicalstore", port=3306)


python main.py
Menu Options:

1. Add Medicine: Add a new medicine record by providing its details.
2. View Medicines: View all medicine records stored in the database.
3. Update Medicine: Update a medicine record by entering its ID and the new details.
4. Delete Medicine: Delete a medicine record by entering its ID.
5. Exit: Exit the application.
Example Usage
To add a new medicine:

Enter your choice: 1
Enter medicine name: Paracetamol
Enter category: Painkiller
Enter price: 20.50
Enter quantity: 100
Enter manufacturer: XYZ Pharma
Enter expiry date (YYYY-MM-DD): 2024-12-31
To view all medicines:

Enter your choice: 2
To update a medicine:


Enter your choice: 3
Enter medicine ID to update: 1
Press 1 for Name change
Press 2 for Price change
Press 3 for Quantity change
To delete a medicine:

Enter your choice: 4
Enter ID to delete: 1
Are you sure to delete this record? (y/n) y


Troubleshooting
Connection Errors: Ensure MySQL server is running and that your credentials are correct.
Table/Column Issues: Double-check the table structure and column names to ensure they match your SQL commands.








