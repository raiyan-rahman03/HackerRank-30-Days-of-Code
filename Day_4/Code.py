class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
             self.age=initialAge   
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        a=self.age
        if a<13:
            print("You are young.")
        elif a >=13 and a<18:
             print("You are a teenager.")  
        else:
             print("You are old.")     
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.age+=1
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")