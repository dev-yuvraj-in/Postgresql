import psycopg2 

conn = psycopg2.connect(
    host="localhost",
    dbname="students",
    user="postgres",
    password="****",
    port=5432
)

cur = conn.cursor()

cur.execute("SELECT * FROM student_info;")

rows = cur.fetchall()  # Get all rows

for row in rows:
    print(row)

conn.commit()

cur.close()
conn.close()