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

def delete_data():
    student_id = input("Enter the ID of the student you want to delete: ")
    conn=psycopg2.connect(dbname="studentdb",user="postgres",password="00RaiserG#",host="localhost",port="5432")
    cur=conn.cursor()

    cur.execute("select * from students where student_id=%s",(student_id,))
    student = cur.fetchone()

    if student:
        print(f"Student to be deleted: ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}")
        choice = input("Are you sure you want to delete the student? (yes/no)")
        if choice.lower() == "yes":
            cur.execute("delete from students where student_id = %s",(student_id,))
            print("Student record deleted.")
        else:
            print("Deletion cancelled.")
    else: 
        print("Student not found.")

    conn.commit()
    conn.close()


def update_data():
    student_id = input("Enter id of the student to be updated: ")
    conn=psycopg2.connect(dbname="studentdb",user="postgres",password="00RaiserG#",host="localhost",port="5432")
    cur=conn.cursor()
    fields = {
        "1":("name","Enter the new name: "),
        "2":("address","Enter the new address: "),
        "3":("age","Enter the new age: "),
        "4":("number","Enter the new number: "),
    }
    print("Which field would you like to update? ")
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    field_choice = input("Enter the number of the field you want to update: ")
    
    if field_choice in fields:
        field_name, prompt = fields[field_choice]
        new_value = input(prompt)
        sql = f"update students set {field_name} = %s where student_id=%s"
        cur.execute(sql,(new_value,student_id))
        print(f"{field_name} updated successfully.")
    else:
        print("Invalid choice.")
    
    conn.commit()
    conn.close()

def read_data():
    conn=psycopg2.connect(dbname="studentdb",user="postgres",password="00RaiserG#",host="localhost",port="5432")
    cur=conn.cursor()
    cur.execute("select * from students;")
    students = cur.fetchall()
    for student in students:
        print(f"Student to be deleted: ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}")

    conn.commit()
    conn.close()


while True:
    print("\n Welcome to the student database management system!")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice=='1':
        create_table()
    elif choice=='2':
        insert_data()
    elif choice=='3':
        read_data()
    elif choice=='4':
        update_data()
    elif choice=='5':
        delete_data()
    elif choice=='6':
        break
    else:
        print("Invalid choice, please enter a number between 1 to 6: ")
        