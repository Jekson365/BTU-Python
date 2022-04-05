

# დავალება !
class Fruit:
    def __init__(self,weight,name):
        self.weight = weight
        self.name = name 
    def __add__(self,other):
        return self.weight + other.weight
    def __eq__(self,other):
        return self.name == other.name


s1 = Fruit(25,"Apple")
s2 = Fruit(15,"Banana")
s3 = Fruit(45,"Banana")

print(s1 == s2)
print(s1.weight + s2.weight + s3.weight)

s3 = Fruit(20,"banana")
s4 = Fruit(23,"banana")

print(s3 + s4)
print(s3 == s4)


#დავალება 2 

import sqlite3

connection = sqlite3.Connection("morty.db")

cursor = connection.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS Dogs (name STRING,age INTEGER,color STRING)")

dogs = [
    ("Jackson",2,'black'),
    ("Chapie",1,'white'),
    ("Boria",1,'light')
]

# cursor.executemany("INSERT INTO Dogs VALUES (?,?,?)",dogs)

select_table = cursor.execute("SELECT * FROM Dogs")

def get_data(database):
    for i in database:
        print(i)
get_data(select_table)


connection.commit()

connection.close()
