class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        
    def introduce_myself(self):
        marital_status = "замужем/женат" if self.is_married else "не замужем/женат"
        return f"{self.fullname}, возраст: {self.age}, семейное положение: {marital_status}"

class Teacher(Person):
    salary = 0
    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = int(experience)
        
    def calculate_salary(self):
        self.salary = 2000 + self.experience * 3000
    
    def introduce_myself(self):
        super_info = super().introduce_myself()
        return f"{super_info}, стаж лет: {self.experience}, зарплата: {self.salary}"
    
    
    
teacher_1 = Teacher("Syimyk", "20", False, "3")
teacher_1.calculate_salary()
print(teacher_1.introduce_myself())

