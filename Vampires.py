class Vampire:
    coven = []
# Vampire class that stores a list
# name, age, an in_coffin, drank_blood_today.
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.in_coffin = True
        self.drank_blood_today = False

# unset the vampires leave their coffins in search of blood
# If don't drink blood and get back to their coffins before sunrise
# they die.


    @classmethod
    def create(cls, name, age):
        vampire = Vampire(name, age)
        cls.coven.append(vampire)
        return vampire


    def drink_blood(self):
            self.drank_blood_today = True
    
#removes from the coven any vampires
# who are out of their coffins
# or who haven't drank any blood in the last day
    @classmethod
    def sunrise(cls):
        for vampire in Vampire.coven:
            if not vampire.in_coffin or not vampire.drank_blood_today:
                return Vampire.coven.remove(vampire)

#sets drank_blood_today and in_coffin to false
# for the entire coven as they go out in search of blood
    def __repr__(self):
        return self.name



    @classmethod
    def sunset(cls):
        for self in Vampire.coven:
            self.drank_blood_today = False
            self.in_coffin = False

#go_home, in_coffin to True   
    def go_home(self):
        self.in_coffin = True
    
    
first = Vampire.create('mark', 8)
second = Vampire.create('york', 10)
Vampire.sunset()
print(Vampire.coven)
first.drink_blood()
first.go_home()
second.go_home()
Vampire.sunrise()
print(Vampire.coven)