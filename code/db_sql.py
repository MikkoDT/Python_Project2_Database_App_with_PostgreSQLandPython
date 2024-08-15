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

    conn=psycopg2.connect(dbname="studentdb",user="postgres",password="00RaiserG#",host="localhost",port="5432")
    cur=conn.cursor()
    
    conn.commit()
    conn.close()

#insert_data()
update_data()