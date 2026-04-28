import db
conn = db.get_connection()
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS game_sessions, players CASCADE;")
conn.commit()
cur.close()
conn.close()
print("Database cleared!")