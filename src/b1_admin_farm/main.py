class Egg:
    def __init__(self):
        self.height = 10
        self.radius = 2
        self.color = "White"

class EggsBox:
    def __init__(self):
        self.eggs: list[Egg] = []
        self.max_capacity: int = 6
    
    def add_egg(self, egg_to_add: Egg):
        if (len(self.eggs) < self.max_capacity):
            if (egg_to_add not in self.eggs):
                self.eggs.append(egg_to_add)
    
def main():
    egg1 = Egg()
    egg2 = Egg()
    egg3 = Egg()

    box = EggsBox()
    box.add_egg(egg1)
    box.add_egg(egg1)
    box.add_egg(egg2)

    





main()