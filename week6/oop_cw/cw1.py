class person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def introduction(self):
        print (f"HI i  {self.name},{self.age} years old")

    def change_address(self, new_address):
        self.address = new_address

p = person("ali",18,"Tehran" )
p.introduction()
