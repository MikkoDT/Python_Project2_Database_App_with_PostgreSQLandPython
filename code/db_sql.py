import psycopg2

def create_table():
    conn=psycopg2.connect(dbname="studentdb",user="postgres",password="00RaiserG#",host="localhost",port="5432")
    cur=conn.cursor()
    #print(conn)
    cur.execute("create table students(student_id serial primary key, name text, address text,age int, number text);")
    print("Student table created")
    conn.commit()
    conn.close()

def insert_data():
    #code to accept data from the user
    name = input("Enter name: ")
    address = input("Enter Address: ")
    age = input("Enter age: ")
    number = input("Enter number: ")
    conn=psycopg2.connect(dbname="studentdb",user="postgres",password="00RaiserG#",host="localhost",port="5432")
    cur=conn.cursor()
    #print(conn)
    cur.execute("insert into students(name,address,age,number) values (%s,%s,%s,%s)",(name,address,age,number))
    print("data added in student table")
    conn.commit()
    conn.close()

def update_data():
    student_id = input("Enter id of the student to be updated: ")
    fields = {
        "1":("name","Enter the new name"),
        "2":("address","Enter the new address"),
        "3":("address","Enter the new age"),
        "2":("address","Enter the new number"),

    }
    name = input("Enter name: ")
    address = input("Enter Address: ")
    age = input("Enter age: ")
    number = input("Enter number: ")
    conn=psycopg2.connect(dbname="studentdb",user="postgres",password="00RaiserG#",host="localhost",port="5432")
    cur=conn.cursor()
    cur.execute("update students set name = %s ,address = %s , age = %s , number = %s where student_id = %s",(name,address,age,number,student_id))
    conn.commit()
    conn.close()

#insert_data()
update_data()