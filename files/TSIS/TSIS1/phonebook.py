import json 
from connect import get_connection

conn = get_connection()
cur = conn.cursor()

def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group = input("Group: ")
    
    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
    g = cur.fetchone()
    group_id = g[0] if g else None
    
    if not g:
        cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (group,))
        group_id = cur.fetchone()[0]
        
    cur.execute("""
        INSERT INTO contacts(name,email,birthday,group_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """, (name, email,birthday, group_id))
    
    contact_id = cur.fetchone()[0]
    
    while True:
        phone = input("Phone (enter to stop): ")
        if not phone:
            break
        ptype = input("Type  (home/work/mobile): ")
        cur.execute("""
            INSERT INTO phones(contact_id, phone, type)
            VALUES (%s,%s,%s)
        """, (contact_id, phone, ptype))
        
    conn.commit()
    
def view_contacts():
    cur.execute("""
        SELECT c.id, c.name, c.email, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        ORDER BY c.name
    """)
    
    for row in cur.fetchall():
        print(row)
        
def search():
    q = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    for r in cur.fetchall():
        print(r)
    
def filter_group():
    g = input("Group: ")
    cur.execute("""
        SELECT c.name, c.email
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name=%s         
    """, (g,))
    for r in cur.fetchall():
        print(r)
        
def pagination():
    limit = 3
    offset = 0
    
    while True:
        cur.execute("""
            SELECT name, email FROM contacts
            ORDER BY id
            LIMIT %s OFFSET %s          
    """, (limit, offset))
    
        rows = cur.fetchall()
        for r in rows:
            print(r)
        
        cmd = input("n-next, p-prev, q-quit: ").lower()
        if cmd == "n":
            offset+= limit
        elif cmd == "p" and offset >= limit:
            offset -= limit
        else:
            break
        
def export_json():
    cur.execute("SELECT * FROM contacts")
    contacts = []
    
    for c in cur.fetchall():
        cur.execute("SELECT phone, type FROM phones WHERE contact_id=%s", (c[0],))
        phones = [{"phone":p,"type":t} for p,t in cur.fetchall()]
        
        contacts.append({"id":c[0],"name":c[1],"email":c[2],"birthday":str(c[3]), "group_id":c[4],"phones":phones})
        
        with open("contacts.json", "w") as f:
            json.dump(contacts,f,indent=4)
            
def import_json():
    with open("contacts.json") as f:
        data=json.load(f)
        
    for c in data:
        cur.execute("SELECT id FROM contacts WHERE name=%s",(c["name"],))
        ex = cur.fetchone()
            
        if ex:
            ans=input("Overwrite? y/n: ")
            if ans=="n":
                continue
            cid=ex[0]
            cur.execute("DELETE FROM phones WHERE contact_id=%s",(cid,))
        else:
            cur.execute("INSERT INTO contacts(name,email,birthday,group_id) VALUE(%s,%s,%s,%s) RETURNING id",
                        (c["name"],c["email"],c["birthday"],c["group_id"]))
            cid=cur.fetchone()[0]
                
        for p in c["phones"]:
            cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES(%s,%s,%s)",
                        (cid,p["phone"],p["type"]))
            
    conn.commit()
    

while True:
    print("\n1 Add, 2-View, 3-Search, 4-Filter, 5-Page, 6-Export, 7-Import, 0-Exit")
    chc = input("Choose: ")
    
    if chc == "1": add_contact()
    elif chc == "2": view_contacts()
    elif chc == "3": search()
    elif chc == "4": filter_group()
    elif chc == "5": pagination()
    elif chc == "6": export_json()
    elif chc == "7": import_json()
    else:
        break

conn.commit()
cur.close()
conn.close()        