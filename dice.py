import random

class Dice(object):
    def __init__(self, input_data):
        print("2. __init__ started. input data =", input_data)
        self.store_data = input_data
        print("3. input data -> self.store_data =", self.store_data)

    def roll(self):
        print("4. roll function called.")
        return random.randint(1, self.store_data)


print("1. Start rolling 6 sides dice")
s = Dice(6)
print("5. dice roll:", s.roll())
print("dice roll:", s.roll())
print("dice roll:", s.roll())

print("Start rolling 20 sides die")
sb = Dice(20)
print("dice roll:", sb.roll())
print("dice roll:", sb.roll())
