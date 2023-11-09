
# a class and object
class User:
    def __init__(self,name, age ,location):
        self.name = name
        self.age = age
        self.location = location
# a function returning the location        
    def myfunction(self):
      print(self.location)
person =User("sheillah",22,"kabowa")
#concatenating to return name and age
print (person.name, person.age)     
 
# a function that prints user location

person.myfunction()    
    



