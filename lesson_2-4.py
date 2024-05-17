# тема магические методы
# dunder методы - (double underscore)"

# class BrawlStars:
#     def __init__(self, hero, map, coins):
#         self.hero = hero
#         self.map = map
#         self.coins = coins

#     def info(self):
#         print(f"Hero - {self.hero}, map - {self.map}, coins - {self.coins}")
        
#     # def __repr__(self): # print
#     #     return f"Hero - {self.hero}, map - {self.map}, coins - {self.coins} \nэто repr"
    
#     def __str__(self): # print
#         return f"Hero - {self.hero}, map - {self.map}, coins - {self.coins} \nэто str"
    
#     def __call__(self, a,b):
#         print("Это магический метод call")
#         return a , b



# brawl = BrawlStars("Spike", "School", 200000)
# print(brawl)
# # print(brawl.hero)
# # brawl.info()

# brawl(3,7)



class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def __str__(self):
        return f"имя - {self.name},элктронная почта - {self.email},телефон - {self.phone}"
meder = GeeksPeople("meder", "meder@example.com", "xaomi")
print(meder)

class Studente(GeeksPeople):
    def __init__(self, name, email, phone, studente_id,group_where_study):
        GeeksPeople.__init__(self,name, email, phone)
        self.studente_id = studente_id
        self.group_where_study = group_where_study
    def study(self):
        print(f"имя - {self.name},учится в группе-{self.group_where_study}")
Aslan = Studente("meder", "meder@gmail.com", "xaomi",123456533433,"17-2b")
Aslan.study()

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        GeeksPeople.__init__(self,name, email, phone)
        self. teacher_id = teacher_id
        self.group_where_teach = group_where_teach
    def teach(self):
        print(f"имя - {self.name},препадает группе-{self.group_where_teach}")
Syimyk = Teacher("Syimyk","Syimyk@gmail.com","apple",47327598,"17-2b")
Syimyk.teach()

class Admin(GeeksPeople):
    def __init__(self, name, email, phone,admin_id):
        GeeksPeople.__init__(self,name, email, phone)
        self.admin_id = admin_id
    def creat_group(self):
        print(f"{self.name}-создал группу")

admin = Admin('ulan','ulan@gmail.com','apple',23246578)   
admin.creat_group()
class Mentor(Studente,Teacher):
    def __init__(self, name, email, phone, studente_id, group_where_study,teacher_id, group_where_teach):
        Teacher.__init__(self,name, email, phone, studente_id, group_where_study)
        Studente.__init__(self,name, email, phone,teacher_id, group_where_teach )
mentor = Mentor("aslan","aslan@example.com","apple",123456533433,"17-2b",47327598,"19-2b")
mentor.teach()
mentor.study()




    
    

        



    









    