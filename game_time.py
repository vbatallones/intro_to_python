class Gametime():
    def __init__(self, gen, types, role ):
        self.role = role
        self.type = types
        self.gen = gen

    def heroClass(self, heroRole):
        self.role = heroRole

    def heroType(self, type_of_hero):
        self.type = type_of_hero

    def heroGender(self, gender):
        self.gen = gender


karina = Gametime("female", "Mage", "Assassin")

karina.heroClass("killer")
print("Karina is a {}".format(karina.role))