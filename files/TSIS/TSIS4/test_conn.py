import psycopg2

try:
    
    conn = psycopg2.connect(
        host="localhost",
        database="postegres",
        user="postgres",
        password="1234" 
    )
    print("connected!")
    conn.close()
except Exception as e:
    print(f"Error: {e}")