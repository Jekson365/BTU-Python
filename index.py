#დავალება 1 

class Calculator:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def sum(self):
        print(self.x + self.y) #შეკრება

    def sub(self):
        print(self.x - self.y) #გამოკლება

    def div(self):
        print(self.x / self.y) #გაყოფა

    def mul(self):
        print(self.x * self.y) #გამრავლება

    
calculator_object = Calculator(10,5)


 
#დავალება 2 

class Employee:
    def __init__(self,name,surname,age,salary):
        self.name = name 
        self.surname = surname
        self.age = age 
        self.salary = salary
    def min_salary(self):
        print(f"მომხამრებელი რომელსაც ყყველაზე დაბალი ხელფასი აქვს : {self.name} , {self.surname} , {self.age} , {self.salary}")
    def oldest(self):
        print(f" ყველაზე ხნიერი მომხამრებელი : {self.name} , {self.surname} , {self.age} , {self.salary}")

#ცარიელი ლექსიკონიო
empty_dict = {
    "name":[],
    "age":[],
    "surname":[],
    "salary":[]
}

datas = open("dataset1.csv","r") #ტექსტური ფაილის შემოტანა
next(datas)


splited_data = datas.read().split() #ფაილის დასპლიტვა
 


for i in range(len(splited_data)): #ლუპი ამატებს ელემენტებს Empty_dict - ში 
    splited_with_coma = splited_data[i].split(",")
    empty_dict["name"].append(splited_with_coma[0])
    empty_dict["age"].append(splited_with_coma[2])
    empty_dict["surname"].append(splited_with_coma[1])
    empty_dict["salary"].append(splited_with_coma[3])



min_salary = min(empty_dict["salary"])
min_salary_index = empty_dict["salary"].index(min_salary) #იმ ადამიანის ინდექსი  ლექსიკონში რომელსაც ყველაზე დაბალი ხელფასი აქვს

 
 
#ინდექსის მიხედვით ადამიანის სახელის , გვარის , ასაკის და ხელფასის ცვლადებში მოთავსება
name_data = empty_dict["name"][min_salary_index] 
age_data = empty_dict["age"][min_salary_index]
surname_data = empty_dict["surname"][min_salary_index]
salary_data = empty_dict["salary"][min_salary_index]


# ყველაზე დიდი ასაკი და მისი ინდექსი
max_age = max(empty_dict["age"])
max_age_index = empty_dict["age"].index(max_age)

#ინდექსის მიხედვით ადამიანის სახელის , გვარის , ასაკის და ხელფასის ცვლადებში მოთავსება
name_data_1 = empty_dict["name"][max_age_index] 
age_data_2 = empty_dict["age"][max_age_index]
surname_data_3 = empty_dict["surname"][max_age_index]
salary_data_4 = empty_dict["salary"][max_age_index]

 


emp_obj = Employee(name_data,age_data,surname_data,salary_data).min_salary() # მონაცემების კლასისთვის მიწოდება და დაბეჭდვა 
emp_obj_2 = Employee(name_data_1,age_data_2,surname_data_3,salary_data_4).oldest() # მონაცემების კლასისთვის მიწოდება და დაბეჭდვა 

 

