# /# class person:
# #     def __init__(self,fname,lname):
# #         self.name=fname
# #         self.namee=lname
# #     def printname(self):
# #         print(self.name,self.namee)
# # x=person("ASMA","SHERIN")
# # x.printname()
#
#
# # class animal:
# #     def speak(self):
# #         return "animal sound"
# # class dog:
# #     def bark(self):
# #         return "woof"
#
#
# # class vehicle:
# #     def __init__(self,company,model,color,fuel):
# #         self.company1=company
# #         self.model1=model
# #         self.color1=color
# #         self.fuel1=fuel
# #     def start(self):
# #         print("starting engine")
# #     def change(self):
# #         print("changing gear")
# # class car(vehicle):
# #     def openn(self):
# #         print("open sunroof")
# # c1=car("bmw","x4","black","diesel")
# # c1.openn()
# # c1.change()
# # c1.start()
#
#
#
# # class vehicle:
# #     def __init__(self,company,model,color):
# #         self.company=company
# #         self.model=model
# #         self.color=color
# #     def start(self):
# #         print("starting the engine")
# # class car(vehicle):
# #     def __init__(self,company,model,color,fuel):
# #         super().__init__(company,model,color)
# #         self.fuel=fuel
# #     def open(self):
# #         print("opening the sunroof")
# # c1=car("bmw","x4","black","diesel")
# # print(c1.color)
# # print(c1.fuel)
#
#
#
# # singleinheritance
# # class people:
# #     def speak(self):
# #         print("people are speaking")
# # class men(people):
# #     def talk(self):
# #         print("men are talking")
# # obj=men()
# # obj.talk()
# # obj.speak()
#
#
# # multilevelinheritance
# class people:
#     def speak(self):
#         print("people are speaaking")
# class men(people):
#     def talk(self):
#         print("men are talking")
# class child(men):
#     def eat(self):
#         print("child is eating")
# obj=child()
# obj.eat()
# obj.talk()
# obj.speak()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
for x in range(1,10):
    print(x)