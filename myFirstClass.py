__author__ = 'kwoshvick'

class PartyAnimal:

    x = 0
    name = ''

    def __init__(self,nam):
        self.name = nam
        print(self.name, ' constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, ' Party count ', self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jack")
j.party()
s.party()




