# usinginit
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("john",15)
# print(p1.name)
# print(p1.age)



# withoutstr
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("john",15)
# print(p1)


# withstr
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}({self.age})"
# p1=person("john",15)
# print(p1)



# objectmethods
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print("my name is ",self.name)
#         print("my age is ",self.age)
# p1=person("john",15)
# p1.myfunc()


# modify
# class person:
#      def __init__(self,name,age):
#          self.name=name
#          self.age=age
#      def myfunc(self):
#          print("my name is ",self.name)
#          print("my age is ",self.age)
# p1=person("john",15)
# p1.age=30
# p1.name="annu"
# p1.myfunc()

# deleteobjectprprt
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myfunc(self):
#         print("my name is ", self.name)
#         print("my age is ", self.age)
# p1 = person("john", 15)
# del p1.name
# print(p1.name)



# deleteobjects
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myfunc(self):
#         print("my name is ", self.name)
#         print("my age is ", self.age)
# p1 = person("john", 15)
# del p1
# print(p1)


# inheritance
# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def greet(self):
#         print(self.firstname,self.lastname)
# class student (person):
#     def __init__(self,fname,lname):
#         person.__init__(self,fname,lname)
# x=student("Asma","Sherin")
# x.greet()



# class person:
#     def __init__(self,name,age):
#         self.fname=name
#         self.fage=age
# p1=person("john",15)
# print(p1.fage)
# print(p1.fname)


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("john",15)
# print(p1)



# class person:
#     def __init__(self,name,age):
#         self.fname=name
#         self.fage=age
#     def __str__(self):
#         return f"{self.fname},({self.fage})"
# p1=person("john",15)
# print(p1)



# class Student:
#     def __init__(self,name,age):
#         self.fname=name
#         self.fage=age
# st=Student("john",12)
# print(st.fname)
# print(st.fage)




# class Employee:
#     location="America"
#     company="ABCD"
#     def __init__(self,id,name,salary):
#         self.emp_id=id
#         self.emp_name=name
#         self.emp_salary=salary
#     def get_display(self):
#         print(self.emp_id,self.emp_name,self.emp_salary)
# obj1=Employee(1,"asma",50000)
# obj2=Employee(1,"asma",50000)
# obj1.get_display()
# obj2.get_display()
# print(obj1.emp_salary)


#object/instance method
# class Student:
#     school="abcd"
#     def __init__(self,roll_no,name,study_class,teacher):
#         self.roll=roll_no
#         self.name=name
#         self.classs=study_class
#         self.teach=teacher
#     def get_display(self):
#         print(f"roll:{self.roll}\nname:{self.name}\nclass:{self.classs}\nteach:{self.teach}\nschool name:{Student.school}")
#     def marks(self,phy,chem,math):
#         self.physics=phy
#         self.chemistry=chem
#         self.maths=math
#     def avg_marks(self):
#         return (self.physics+self.chemistry+self.maths)/3
# s1=Student(1,"asma","5th","aysha")
# s2=Student(2,"sherin","10th","annu")
#
# s1.get_display()
# s1.marks(20,20,30)
# print(s1.avg_marks())
# print("---------------------------------------------------------")
# s2.get_display()
# s2.marks(20,30,30)
# print(s2.avg_marks())




# classmethod
# class Student:
#     school="abcd"
#     def __init__(self,roll_no,name,study_class,teacher):
#         self.roll=roll_no
#         self.name=name
#         self.classs=study_class
#         self.teach=teacher
#     def get_display(self):
#         print(f"roll:{self.roll}\nname:{self.name}\nclass:{self.classs}\nteach:{self.teach}\nschool name:{Student.school}")
#     @classmethod
#     def school_name(cls):
#         print("school name:",cls.school)
# Student.school_name()


# staticmethod
class Student:
    school="abcd"
    def __init__(self,roll_no,name,study_class,teacher):
        self.roll=roll_no
        self.name=name
        self.classs=study_class
        self.teach=teacher
    def get_display(self):
        print(f"roll:{self.roll}\nname:{self.name}\nclass:{self.classs}\nteach:{self.teach}\nschool name:{Student.school}")
    @staticmethod
    def about():
        print("it is best")
Student.about()





# access instance variable
# class Student:
#     def __init__(self,name,age):
#         self.name1=name
#         self.age1=age
# s1=Student("john",1)
# print(s1.name1,s1.age1)
# s1.age1=10
# print(s1.name1,s1.age1)
# s1.year=1234
# print(s1.name1,s1.age1,s1.year)



# # collection item has instance in list
# class Student:
#     def __init__(self,name,roll,marks:list):
#         self.name1=name
#         self.roll1=roll
#         self.marks1=marks
#     def display(self):
#         print(f"name:{self.name1},roll:{self.roll1},marks:{self.marks1}")
#     def find_percentage(self):
#         total=0
#         for i in self.marks1:
#             total=total+i
#         perc=(total/400)*100
#         print("percentage is:",perc)
# s1=Student("alen","67",[10,0,30,40])
# s1.display()
# s1.find_percentage()





# collection item has instance in dictionary
# class Student:
#     def __init__(self,name,roll,marks:dict):
#         self.name1=name
#         self.roll1=roll
#         self.marks1=marks
#     def display(self):
#         print(f"name:{self.name1},roll:{self.roll1},marks:{self.marks1}")
#     def find_percentage(self):
#         total=0
#         for i in self.marks1.values():
#             total=total+i
#         perc=(total/400)*100
#         print("percentage is:",perc)
# s1=Student("alen","67",{"phy":10,"chem":60})
# s1.display()
# s1.find_percentage()




# class company:
#     def __init__(self,name,location,manager):
#         self.c_name=name
#         self.c_location=location
#         self.c_manager=manager
# class employee:
#     def __init__(self,id,age,cmp:company):
#         self.id=id
#         self.age=age
#         self.company=cmp
#     def details(self):
#         print(f"id:{self.id},age:{self.age},cmp={self.company.c_name}")
# c1=company("john","america","jaay")
# e1=employee("120","10,",c1)
# e1.details()



































































































