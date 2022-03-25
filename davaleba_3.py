import sqlite3

from matplotlib.pyplot import connect 

connection = sqlite3.connect("census.db")

cursor = connection.cursor()
# cursor.execute("CREATE TABLE denisty (province_or_teritory TEXT ,population INTEGER,land_area REAL) ")

table_1 = [
    ("Newfoundland and labrador",512930,370501.1),
    ("Prince Edward Island",2314532,238321.9),
    ("Nova Scotia",321432132,348293.49),
    ("New Brunswick",31233,37234.39),
    ("Quebec",54631243,37121.213),
    ("Saskatchewan",54232143,54801.122),
    ("British Columbia",64243,23.41),
    ("Yukon Territory",51322930,2312.21),
    ("Northwest Territories",512930,1329.31),
    ("Nunavut",321330,2319.31),
]


# cursor.executemany("INSERT INTO denisty VALUES (?,?,?)",table_1)

cursor.execute("SELECT * FROM denisty")
# # print items from database
# # for i in cursor.fetchall():
# #     print(i)

x = cursor.fetchall()

# POPULATION
# for i in x:
#     print(i[0])
class Fetcher:
    def __init__(self,mydatabase):
        self.mydatabase = mydatabase
    def population(self): # მოსახლეობა
        for i in self.mydatabase:
            print(i[0])
    def less_than_1(self): # 1 მილიონზე ნაკლები ადამიანი
        for i in self.mydatabase:
            if i[1] < 1000000:
                print(i[0])
    def task_7(self): # 1 მილიონზე ნაკლები ან 5 მილიონზე მეტი ადამიანი
        for i in self.mydatabase:
            if i[1] < 100000 or i[1] > 5000000:
                print(i[0])

    def task_8(self): # 1 მილიონსა და 5 მილიონს შორის
        for i in self.mydatabase:
            if 1000000 < i[1] < 5000000:
                print(i[0])

    def task_9(self): # 2000000 მეტი ფართობი
        for i in self.mydatabase:
            if i[2] > 200000:
                print(i[0])

    def task_10(self): # სიმჭიდროვე
        for i in self.mydatabase:
            print(i[1] / i[2])




fetcher = Fetcher(x)

fetcher.task_10()




connection.commit()
print("success!")
connection.close()