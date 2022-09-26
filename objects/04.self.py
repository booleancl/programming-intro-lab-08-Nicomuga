# Podemos utilzar el método especial  __init__ (conocido como constructor)
# y el objeto actual self para hacer un creador de objetos del tipo definido con la
# palabra reservada class
# 

class Student:
    def __init__(self, name, position, skills ):
        self.name = name
        self.position = position
        self.skills = skills
    def present_self(self):
        print('My name is', self.name +',', "i'am a", self.position, 'nd my skills are', self.skills)


alice_skills = ["Python", "Git", "HTML","CSS","Javascript"]
alice = Student('Alice', 'Fullstack Developer', alice_skills )
bob = Student('Bob', 'Chef', 'to cook ñami meals')
alice.present_self()