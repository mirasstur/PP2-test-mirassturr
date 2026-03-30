import psycopg2

# 1. Объявляем переменную заранее
connection = None

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="testdb", 
        user="postgres",
        password="1234" 
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    print(f"Вы подключены к: {cursor.fetchone()}")

except Exception as error:
    print(f"Ошибка подключения: {error}")

finally:
    # Теперь Python знает, что такое connection, даже если подключение не удалось
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто.")