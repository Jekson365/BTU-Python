

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
s3 = Fruit(15,"Banana")
s4 = Fruit(45,"Banana")

print(s1 == s2)
print(s1.weight + s2.weight + s3.weight + s4.weight)


s5 = Fruit(20,"banana")
s6 = Fruit(23,"banana")
s7 = Fruit(43,"banana")

print(s5 + s6)
print(s5 == s6 == s7)

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
