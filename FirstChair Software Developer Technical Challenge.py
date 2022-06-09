#FirstChair Software Developer Technical Challenge

#Chosen Challenge: Challenge #1 - Object Oriented Programming concepts
#Chosen programming language: Python



# Zoo class

class Zoo:
    
    day = []
    def __init__( self , Name, City, Operating_Hours, day = []):
        self.Name = Name
        self.City = City
        self.Operating_Hours = Operating_Hours
        Zoo.day = day
         
    def print(self):
        print("Name: {}".format(self.Name))
        print("City: {}".format(self.City))
        print("Operating_Hours: {}".format(self.Operating_Hours))
    
     
    def ticket_price(self, day):
        if day in Zoo.day == "Monday" or "Tuesday" or "Thursday" or "Friday":
            print("The ticket price is: $19.99")
        elif day in Zoo.day == "Wednesday":
            print("The ticket price is: $9.99")
        elif day in Zoo.day == "Saturday" or "Sunday":
            print("The ticket price is: $25.99")
        else:
            print("Error: Incorrect entry")

        

# Animal class (represent an Animal that lives in the Zoo)
# Define what happens when a new animal object is created

class Animal:
    
    Animals = [] 
    def __init__(self , Animal_Species, Name, Number_of_Legs, Gender, Animals = []):
        self.Animal_Species = Animal_Species
        self.Name = Name
        self.Number_of_Legs = Number_of_Legs
        self.Gender = Gender
        Animal.Animals = Animals
    
    def add_animal(self, a):
        Animal.Animals.append(a)
    
    def remove_animal(self, a): 
        Animal.Animals.remove(a)
    
    def show_animal(self):
        for a in Animal.Animals:
            print(a)

    def to_print(self): 
        print("Animal_Species: {}".format(self.Animal_Species))
        print("Name: {}".format(self.Name))
        print("Number_of_Legs: {}".format(self.Number_of_Legs))
        print("Gender: {}".format(self.Gender))
         


# 3 additional Classes that extend the Animal Class and represent 3 different species

class Giraffe(Animal): 
    
    def Giraffe_Details(self, current_height):
        self.current_height = current_height
   
    def comparison(self):
        if self.current_height >= 5.5:
            print ("The Giraffe is male")
        else:
            if self.current_height <= 4.6:
                print ("The Giraffe is female")

            
class Crocodile(Animal): 
    
    def Crocodile_Details(self, number_of_teeth):
        self.number_of_teeth = number_of_teeth    
    
class Tortoise(Animal):   
    
    def Tortoise_details(self, current_age):
        self.current_age = current_age
    
    def size(self):
        if self.current_age < 50:
            print ("The Tortoise is young")
        elif self.current_age >= 50 and self.current_age >= 100:
            print ("The Tortoise is middle-aged")
        else:
            if self.current_age >100:
                print ("The Tortoise is old")