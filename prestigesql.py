import psycopg2

from Student import Student

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="CampNou2021",
    port=5432
)
cur = conn.cursor
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name text,
    age INT,
    grade  text
)
""")


student1 = Student(id = 123456789, grade = '10', age = 15, name = 'Moshe')
student2 = Student(id = 654456789, grade = '11', age = 14, name = 'Noam')
student3 = Student(id = 123432489, grade = '12', age = 17, name = 'Doron Shatz')
cur.execute("""INSERT INTO students(id,name,age,grade) VALUES
(student1.id, student1.name, student1.age, student1.grade)
(student2.id, student2.name, student2.age, student2.grade)
(student3.id, student3.name,student3.age, student3.grade)
""")

cur.execute("""SELECT * from students where name == 'Moshe';""")
for row in cur.fetchall():
    print(row)

sql = cur.mogrify(
    """SELECT * FROM students WHERE name LIKE %s OR age < %s;""",
    ("D%", 15)
)
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
