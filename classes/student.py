import datetime
class Student:
    school="AkiraChix"
    def __init__(self,first_name,last_name,age,country) :
    #    attributes
       self.first_name=first_name
       self.last_name=last_name
       self.age=age
       self.country=country
    def greet_student(self):
        return f"hello {self.name} from {self.country} welcome to {self.school}"
    def show_fullname(self):
     print (f"{self.first_name} {self.last_name}")
     
    def year_of_birth(self):
       return datetime.date.today().year -self.age
       
    def show_initial(self):
       print(self.first_name[0] +" "+ self.last_name[0])
    
# 2






        
    
