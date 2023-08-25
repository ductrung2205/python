class Animal:
    def __init__(self):
        self.name = None
    def speak(self):
        print(None)
        
class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__()
        self.legs = 4
    
    def get_legs(self):
        print('Cat has {} legs'.format(self.legs))
        return self.legs

class Duck(Animal):
    def __init__(self):
        super(Duck, self).__init__()
        self.legs = 2

    def get_legs(self):
        print('Duck has {} legs'.format(self.legs))
        return self.legs

def get_legs(animal):
    legs = animal.get_legs()
    return legs

if __name__ == '__main__':
    cat_one = Cat()
    duck_one = Duck()
    cat_legs = get_legs(cat_one)
    duck_legs = get_legs(duck_one)
    
        