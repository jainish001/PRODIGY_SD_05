

#                                                                              ##TASK - 1
# def convert_from_celsius(c):
#     f = (c * 9/5) + 32
#     k = c + 273.15
#     return f, k

# def convert_from_fahrenheit(f):
#     c = (f - 32) * 5/9
#     k = c + 273.15
#     return c, k

# def convert_from_kelvin(k):
#     c = k - 273.15
#     f = (c * 9/5) + 32
#     return c, f

# print('''Temperature Converter
#        1. Celsius
#        2. Fahrenheit
#        3. Kelvin''')

# choice = input("Enter your choice (1/2/3): ")

# if choice == '1':
#     c = float(input("Enter temperature in Celsius: "))
#     f, k = convert_from_celsius(c)
#     print(f"Fahrenheit: {f:.2f}°F")
#     print(f"Kelvin: {k:.2f}K")

# elif choice == '2':
#     f = float(input("Enter temperature in Fahrenheit: "))
#     c, k = convert_from_fahrenheit(f)
#     print(f"Celsius: {c:.2f}°C")
#     print(f"Kelvin: {k:.2f}K")

# elif choice == '3':
#     k = float(input("Enter temperature in Kelvin: "))
#     c, f = convert_from_kelvin(k)
#     print(f"Celsius: {c:.2f}°C")
#     print(f"Fahrenheit: {f:.2f}°F")

# else:
#     print("Invalid choice. Please enter 1, 2, or 3.")



import random


n = random.randint(1, 100)

a = -1  
guesses = 1 

print("Welcome to the Guessing Game!")
print("Guess the number between 1 and 100")


while a != n:
    a = int(input("Guess the number: "))

    if a > n:
        print("Too high! Try a lower number.")
        guesses += 1
    elif a < n:
        print("Too low! Try a higher number.")
        guesses += 1


print(f" You guessed the number {n} correctly in {guesses} attempts!")






#                                                                              ##TASK - 3


import sqlite3
import csv
from datetime import datetime

def setup_database():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact (
            name REAL NOT NULL,
            contact VARCHAR (100) NOT NULL,
            email TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')



    conn.commit()
    conn.close()
   
 
def save_to_csv(name, contact, email,date):
    with open("contacts.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, contact, email,date])


    

def add_info():
    try:
        name=input("Enter your full name:")
        if name=="":
          print("Name cannot be empty")
          return
        
        contact=input("Enter your contact number:").strip()
        if not contact.isdigit() or len(contact) != 10:
             print("Invalid contact number!")
             
        email= input("Enter your email:")
        if "@" not in email or "." not in email:
            print("Invalid email ID!")
            
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        if date.strip() == "":
            date = datetime.today().strftime('%Y-%m-%d')  
                
        conn=sqlite3.connect('contact.db')
        cursor=conn.cursor()
        cursor.execute('INSERT INTO contact (name,contact,email,date) VALUES (?,?,?,?)',(name,contact,email,date))
        save_to_csv(name,contact,email,date)
        conn.commit()
        conn.close()

    except ValueError:
      print("invalid input please enter the input to valid format")

setup_database()
add_info()        
     



        
def view_contacts():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM contact")
    rows = cursor.fetchall()
    if not rows:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]} | Date: {row[4]}")
    conn.close()
        
def delete_contact():
    view_contacts()
    try:
        contact_id=int(input("Enter the ID of thr contact to delete:"))
        conn=sqlite3.connect("contact.db")
        cursor=conn.cursor()
        cursor.execute("DELETE FROM contact WHERE rowid=?",(contact_id,))        
        conn.commit()
        conn.close()
        print("Contact deleted successfully")
    except ValueError:
        print("Invalid input . Please enter a valid ID")    



def edit_contact():
    view_contacts()
    try:
        contact_id = int(input("Enter the ID of the contact to edit: "))
        new_name = input("Enter new name (leave blank to keep current): ")
        new_contact = input("Enter new contact (leave blank to keep current): ")
        new_email = input("Enter new email (leave blank to keep current): ")

        conn = sqlite3.connect("contact.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contact WHERE rowid = ?", (contact_id,))
        contact = cursor.fetchone()
        if not contact:
            print("Contact not found.")
            return
        
        updated_name = new_name if new_name else contact[0]
        updated_contact = new_contact if new_contact else contact[1]
        updated_email = new_email if new_email else contact[2]

        cursor.execute('''
            UPDATE contact
            SET name = ?, contact = ?, email = ?
            WHERE rowid = ?
        ''', (updated_name, updated_contact, updated_email, contact_id))

        conn.commit()
        conn.close()
        print("Contact updated successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid ID.")
    

def menu():
    while True:
        print("\n====== Contact Saver Menu ======")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Delete Contact")
        print("4. Edit Contact")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                add_info()
            elif choice == 2:
                view_contacts()
            elif choice ==3:
                delete_contact()
            elif choice == 4:
                edit_contact()
            elif choice == 5:
                print(" Exiting... Goodbye!")
                break
            else:
                print(" Invalid choice. Try again.")
        except ValueError:
            print(" Please enter a valid number.")

setup_database()
menu() 




