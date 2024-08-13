import psycopg2

con=psycopg2.connect(dbname="studentdb",user="postgres",password="00RaiserG#",host="localhost",port="5432")
print(con)