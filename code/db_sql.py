import psycopg2

conn=psycopg2.connect(dbname="studentdb",user="postgres",password="00RaiserG#",host="localhost",port="5432")
cur=conn.cursor()
#print(conn)
cur.execute("create table students(student_id serial primary key, name text, address text,age int, number text);")
print("Student table created")
conn.commit()
conn.close()