
class Student:
    name = input("Enter name:  ") # variable if class Students
    age = 12 
    schoolClass = "6th A" 
    Classteacher = "Priya Ma am"  

    def show_Detalis(self): 
        print("the detalis of students are as  :")
        print("Name  :  ", self.name) 
        print("Age  :  ", self.age) 
        print("Class  :  " , self.schoolClass) 
        print("Class teacher : ", self.Classteacher) 


print("\nAge of student :", Student.age) 
print("\n Class teacher name:",Student.Classteacher) 

# creating objects of class Student 
Student1 = Student() 
Student2 = Student()

print() # to get a blank line 
# calling the function to get the detalis
Student1.show_Detalis() 
print() 

Student2.show_Detalis()
