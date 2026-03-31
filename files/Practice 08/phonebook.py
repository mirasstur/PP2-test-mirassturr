import psycopg2
from config import load_config
def manage_phonebook():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                #1 call upsert
                print("--- Adding/Updating ---")
                cur.execute("CALL upset_contacts(%s,%s)", ("Miras Turganbai", "87059198835"))
                
                #2 insert many
                print("--- Insert many ---")
                names = ["Muhit", "Zhiger", "Temir"]
                phones = ["87717441515", "+77075306464", "102"] #one of them invalid
                cur.execute("CALL insert_many_contacts(%s,%s)", (names,phones))
                
                #3 search be pat
                print("--- Search 'Miras' ---")
                cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", ("Miras",))
                for row in cur.fetchall():
                    print(row)
                    
                #4 Paggination
                print("--- Paggination ---")
                cur.execute("SELECT * FROM get_contacts_paged(%s,%s)",(2,0))
                for row in cur.fetchall():
                    print(row)
                    
                #5 delete
                print("--- Delete 'Zhiger' ---")
                cur.execute("CALL delete_contact(%s)", ("Bob",))
                
                conn.commit()
                print("Success")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    
if __name__ == "__main__":
    manage_phonebook()