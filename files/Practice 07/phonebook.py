import psycopg2
from config import load_config
import csv

def get_connection():
    config = load_config()
    return psycopg2.connect(**config)

def create_tables():
    commands= (
    """
    CREATE TABLE IF NOT EXISTS contacts (
        contact_id SERIAL PRIMARY KEY,
        contact_name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20) UNIQUE NOT NULL
    )
    """,
    )
    
    conn = get_connection()
    cur = conn.cursor()
    for command in commands:
        cur.execute(command)
    
    conn.commit()
    cur.close()
    conn.close()
    print("Table Created")

def import_from_csv(file_path):
    conn = get_connection()
    cur = conn.cursor()
    
    with open(file_path,'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                cur.execute(
                    "INSERT INTO contacts (contact_name, phone_number) VALUES (%s, %s)",
                    (row['contact_name'], row['phone_number'])
                )
            except:
                print(f"Missed dublicate: {row}")
                
    conn.commit()
    cur.close()
    conn.close()
    print("CSV import finished")
    
#inserting from console

def insert_from_console():
    name = input("Input the name: ")
    phone = input("Input the number: ")
    
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute(
            "INSERT INTO contacts (contact_name, phone_number) VALUES (%s, %s)",
            (name,phone)
        )
        conn.commit()
        print("Contact added")
    except Exception as e:
        print("Error:", e)
    cur.close()
    conn.close()

#Updating contact

def update_contact():
    name = input("Write the name of contact for update: ")
    new_name = input("New name: ")
    new_phone = input("New number: ")
    
    conn = get_connection()
    cur = conn.cursor()
    
    if new_name:
        cur.execute(
            "UPDATE contacts SET contact_name=%s WHERE contact_name=%s",
            (new_name,name)
        )
    if new_phone:
        cur.execute(
            "UPDATE contacts SET phone_number=%s WHERE contact_name=%s",
            (new_phone, name)
        )
    
    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated!")
    
#Searching/filter

def search_contacts():
    print("1 - by name")
    print("2 - by number")
    choice = input("Choose: ")
    
    conn = get_connection()
    cur = conn.cursor()
    if choice =="1":
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM contacts WHERE contact_name ILIKE %s",
            (f"%{name}%",)
        )
    elif choice == "2":
        prefix = input("Enter number starting: ")
        cur.execute(
            "SELECT * FROM contacts WHERE phone_number LIKE %s",
            (f"{prefix}%",)
        )
        
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
        
    cur.close()
    conn.close()
    
#Deleting

def delete_contact():
    print("1 - Delete by name")
    print("2 - Delete by number")
    choice = input("Choose: ")
    conn = get_connection()
    cur = conn.cursor()
    
    if choice == "1":
        name = input("Name: ")
        cur.execute("DELETE FROM contacts WHERE contact_name=%s", (name,))
        
    elif choice == "2":
        phone = input("Number: ")
        cur.execute("DELETE FROM contacts WHERE phone_number=%s", (phone,))
        
    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted!")
    
def menu():
    while True:
        print("\n Phonebook")
        print("1 - Импорт CSV")
        print("2 - Добавить контакт")
        print("3 - Обновить контакт")
        print("4 - Поиск")
        print("5 - Удалить")
        print("0 - Выход")
        
        choice = input("Choose: ")
        
        if choice == "1":
            import_from_csv(r"C:\Users\Miras\Documents\githowto\githowto\files\Practice 07\contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Wrong choice!")
            

if __name__ == "__main__":
    create_tables()
    menu()