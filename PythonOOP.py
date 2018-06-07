

class Animal():

    def __init__(self, name, legs, arms, sound):
        """Initializes an Animal class."""
        self.name = name
        self.legs = legs
        self.arms = arms
        self.sound = sound

    def speak(self, sound=''):
        """Makes Animal speak another sound."""
        if sound:
            print('I say '+sound+'!')
        else:
            print('I say '+self.sound+'!')

    def describe(self):
        """Describes an Animal."""
        print(
            'I am a ' + self.name + '.\n'
            + 'I have ' + str(self.legs) + ' legs.\n'
            + 'I have ' + str(self.arms) + ' arms.\n'
            + 'I say '+sound+'!'
            )


class SeaCreature(Animal):

    def __init__(self, name, sound, sea_habitat):
        """Initializes a SeaCreature class."""
        Animal.__init__(self, name, 'no', 'no', sound)
        self.sea_habitat = sea_habitat

    def describe(self):
        """Describes a SeaCreature."""
        print(
            'I am a ' + self.name + '.\n'
            + 'I have ' + str(self.legs) + ' legs.\n'
            + 'I have ' + str(self.arms) + ' arms.\n'
            + 'I have fins instead.\n'
            + 'I say ' + self.sound + '!\n'
            + 'I live under the ' + self.sea_habitat + '.'
            )

    def swim(self):
        """Makes a SeaCreature swim."""
        print('I am swimming!')


class LandCreature(Animal):

    def __init__(self, name, legs, arms, sound, land_habitat):
        """Initializes a LandCreature class."""
        Animal.__init__(self, name, legs, arms, sound)
        self.land_habitat = land_habitat

    def describe(self):
        """Describes a LandCreature."""
        print(
            'I am a ' + self.name + '.\n'
            + 'I have ' + str(self.legs) + ' legs.\n'
            + 'I have ' + str(self.arms) + ' arms.\n'
            + 'I say ' + self.sound + '!\n'
            + 'I live in the ' + self.land_habitat + '.'
            )

    def walk(self):
        """Makes a LandCreature walk."""
        print('I am walking!')


class FlyingCreature(Animal):

    def __init__(self, name, legs, sound):
        """Initializes a FlyingCreature class."""
        Animal.__init__(self, name, legs, 'no', sound)
        print('Wings added to Animal')

    def describe(self):
        """Describes a FlyingCreature."""
        print(
            'I am a ' + self.name + '.\n'
            + 'I have ' + str(self.legs) + ' legs.\n'
            + 'I have ' + str(self.arms) + ' arms.\n'
            + 'I have wings.\n'
            + 'I say ' + self.sound + '!\n'
            + 'I can fly.'
            )

    def fly(self):
        """Makes a FlyingCreature fly."""
        print('I am flying!')


class Amphibian(SeaCreature, LandCreature):

    def __init__(self, name, legs, arms, sound, habitat1, habitat2):
        """Initializes an Amphibian class."""
        SeaCreature.__init__(self, name, sound, habitat1)
        LandCreature.__init__(self, name, legs, arms, sound, habitat2)

    def describe(self):
        """Describes an Amphibian."""
        print(
            'I am a ' + self.name + '.\n'
            + 'I have ' + str(self.legs) + ' legs.\n'
            + 'I have ' + str(self.arms) + ' arms.\n'
            + 'I say ' + self.sound + '!\n'
            + 'I live in both ' + self.sea_habitat
            + ' and ' + self.land_habitat + '.'
            )

    def swim_walk(self):
        """Makes an Amphibian swim and walk."""
        walk()
        swim()


fish = SeaCreature('fish', 'blub', 'sea')
fish.describe()
fish.swim()
fish.speak()
fish.speak('hello')
print('\n')
lion = LandCreature('lion', 4, 'no', 'rawr', 'jungle')
lion.describe()
lion.walk()
lion.speak()
lion.speak('hello')
print('\n')
bird = FlyingCreature('bird', 2, 'tweet')
bird.describe()
bird.fly()
bird.speak()
bird.speak('hello')
print('\n')
frog = Amphibian('frog', 4, 'no', 'kokak', 'swamp', 'land')
frog.describe()
frog.walk()
frog.swim()
frog.speak()
frog.speak('hello')
