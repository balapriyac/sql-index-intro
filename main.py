# imports
import sqlite3
from faker import Faker

# connect to the db
db_conn = sqlite3.connect('people_db.db')
db_cursor = db_conn.cursor()

# create table
db_cursor.execute('''CREATE TABLE people (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  email TEXT,
                  job TEXT)''')


# create and insert records
fake = Faker()
Faker.seed(42)

num_records = 100000

for _ in range(num_records):
    name = fake.name()
    email = fake.email()
    job = fake.job()
    db_cursor.execute('INSERT INTO people (name, email, job) VALUES (?,?,?)', (name,email,job))

# commit the transaction and close the cursor and db connection
db_conn.commit()
db_cursor.close()
db_conn.close()
