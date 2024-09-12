import pymysql

def connect_to_db():
    return pymysql.connect(host="localhost", user="root", password="sana", db="medicalstore", port=3306)

def menu():
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Update Medicine")
    print("4. Delete Medicine")
    print("5. Add Customer")
    print("6. View Customers")
    print("7. Place Order")
    print("8. View Orders")
    print("9. Exit")
    choice = int(input("Enter your choice: "))
    return choice
def main():
    while True:
        choice = menu()
        if choice == 1:
            name = input("Enter medicine name: ")
            category = input("Enter category: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            manufacturer = input("Enter manufacturer: ")
            expdate = input("Enter expiry date (YYYY-MM-DD): ")
            add_medicine(name, category, price, quantity, manufacturer, expdate)
        elif choice == 2:
            view_medicines()
        elif choice == 3:
            mid = int(input("Enter medicine ID to update: "))
            name = input("Enter new name (leave blank to skip): ")
            price = input("Enter new price (leave blank to skip): ")
            quantity = input("Enter new quantity (leave blank to skip): ")
            update_medicines(mid, name if name else None, float(price) if price else None, int(quantity) if quantity else None)
        elif choice == 4:
            mid = int(input("Enter medicine ID to delete: "))
            delete_medicine(mid)
        elif choice == 5:
            name=input("Enter Name:")
            email=input("Enter EmailID:")
            phone=int(input("Enter PhoneNumber:"))
            address=input("Enter Address:")
            add_customer(name,email,phone,address)
        elif choice==6:
            view_customers()
        elif choice==7:
             mid=int(input("Enter Medicine ID:"))
             customer_id = int(input("Enter customer ID: "))
             quantity = int(input("Enter quantity: "))
             place_order(customer_id, mid, quantity)
        elif choice==8:
            view_orders()
        elif choice==9:   
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_medicine(name, category, price, quantity, manufacturer, expdate):
    try:
        con = connect_to_db() 
        cr = con.cursor()
        q = f"INSERT INTO medicines (name, category, price, quantity, manufacturer_name, expdate) VALUES ('{name}', '{category}', {price}, {quantity}, '{manufacturer}', '{expdate}')"
        count = cr.execute(q)
        con.commit()
        if count == 1:
            print("Medicine added successfully.")
        else:
            print("Failed to add medicine.")
    except Exception as e:
        print("ERROR: ", e)
    finally:
        con.close()  


def view_medicines():
    try:
        con = connect_to_db()  
        cr = con.cursor()
        q = "SELECT * FROM medicines"  
        cr.execute(q)
        rows = cr.fetchall()  

        if len(rows) == 0:
            print("No medicines found.")
        else:
            
            print("ID".ljust(5), "Name".ljust(20), "Category".ljust(20), "Price".ljust(10), "Quantity".ljust(10), "Manufacturer".ljust(20), "Expiry Date")
            print("-" * 100)

            for row in rows:
                print(str(row[0]).ljust(5), str(row[1]).ljust(20), str(row[2]).ljust(20), str(row[3]).ljust(10), str(row[4]).ljust(10), str(row[5]).ljust(20), str(row[6]))

    except Exception as e:
        print("ERROR: ", e)

    finally:
        con.close()  


def update_medicines(id, name=None, price=None, quantity=None):
    try:
        con = connect_to_db() 
        cr = con.cursor()
        q = f"SELECT * FROM medicines WHERE id='{id}'"
        cr.execute(q)
        if cr.rowcount == 0:
            print("Invalid ID!")
        else:
            r = next(cr)
            print(r[0], r[1], r[2], r[3], r[4], r[5], r[6], sep="\n")
            if name:
                q = f"UPDATE medicines SET name='{name}' WHERE id={id}"
                cr.execute(q)
                print("Name changed.")
            if price:
                q = f"UPDATE medicines SET price={price} WHERE id={id}"
                cr.execute(q)
                print("Price updated.")
            if quantity:
                q = f"UPDATE medicines SET quantity={quantity} WHERE id={id}"
                cr.execute(q)
                print("Quantity updated.")
            con.commit()
    except Exception as e:
        print("ERROR: ", e)
    finally:
        con.close() 


def delete_medicine(mid):
    try:
        con = connect_to_db()  
        cr = con.cursor()
        q = f"SELECT * FROM medicines WHERE id='{mid}'"
        cr.execute(q)
        if cr.rowcount == 0:
            print("Invalid ID!")
        else:
            r = next(cr)
            print(r[0], r[1], r[2], r[3], r[4], r[5], r[6], sep="\n")
            conf = input("Are you sure to delete this record? (y/n): ")
            if conf in ('y', 'Y'):
                q = f"DELETE FROM medicines WHERE id={mid}"
                cr.execute(q)
                con.commit()
                print("Deleted successfully.")
            else:
                print("Delete aborted.")
    except Exception as e:
        print("ERROR: ", e)
    finally:
        con.close()  
def add_customer(name, email, phone, address):
    try:
        q = f"INSERT INTO customers (name, email, phone, address) VALUES ('{name}', '{email}', '{phone}', '{address}')"
        con = connect_to_db()
        cr = con.cursor()
        cr.execute(q)
        con.commit()
        print("Customer added successfully!")
    except Exception as e:
        print("ERROR: ", e)
    finally:
        con.close()
def view_customers():
    try:
        q = "SELECT * FROM customers"
        con = connect_to_db()
        cr = con.cursor()
        cr.execute(q)
        for row in cr:
            print(row)
    except Exception as e:
        print("ERROR: ", e)
    finally:
        con.close()
def place_order(customer_id, medicine_id, quantity):
    try:
        q = f"INSERT INTO orders (customer_id, medicine_id, quantity, order_date) VALUES ({customer_id}, {medicine_id}, {quantity}, CURDATE())"
        con = connect_to_db()
        cr = con.cursor()
        cr.execute(q)
        con.commit()
        print("Order placed successfully!")
    except Exception as e:
        print("ERROR: ", e)
    finally:
        con.close()

def view_orders():
    try:
        q = """SELECT o.id, c.name as customer_name, m.name as medicine_name, o.quantity, o.order_date 
               FROM orders o 
               JOIN customers c ON o.customer_id = c.id 
               JOIN medicines m ON o.medicine_id = m.id"""
        con = connect_to_db()
        cr = con.cursor()
        cr.execute(q)
        for row in cr:
            print(row)
    except Exception as e:
        print("ERROR: ", e)
    finally:
        con.close()


if __name__ == "__main__":
    main()
