class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        #print(args)
        #print(kwargs)
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(self.name, 'снесен, но он останется в историии.')


h1 = House('ЖК Солнечный', 12)
print(House.houses_history)
h2 = House('Хижина люкс', 3)
print(House.houses_history)
h3 = House('ЖК Коммунист', 45)
print(House.houses_history)
del h1
del h2
print(House.houses_history)











