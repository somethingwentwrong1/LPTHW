from sys import exit
from random import randint


# a class that defines enter that contains self integer.
class Scene(object):
    # defined enter as not configured syntax.
    def enter(self):
        print "Not configured. Subclass it and implement enter()."
        exit(1)


# a class that consists of as follows:
class Engine(object):
    # opperates the scene_map by itself.
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('ending')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):

    gg = [
         "You failed to survive.",
         "I think you needed some more skill to play this",
         "Beinging such a coward.",
         "Well basically you suck."
         ]

    def enter(self):
        print Death.gg[randint(0, len(self.gg)-1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "You are Hendrik Hamel whose ship is drifted in Joseon."
        print "After the drift, you are kidnapped in Hyojong's palace."
        print "You're surrounded by people with yellow faces,"
        print "and their language is not understandable."
        print "You can assume that they'll never let you go."
        print "Now, Escape!"
        print "------------------------------------------------------"
        print "You've decided to escape, and now you're in the central"
        print "corridor of the palace."
        print "As you're seeking for the exit, you've found out"
        print "that the soldiers are right in front of you."
        print "You have three choices (type the number)"
        print "1. Go back to the room you were in at the beginning"
        print "2. Fight against the soldiers"
        print "3. Get in to the mysterious room beside you"

        a = int(input("\n>>>"))

        if a == 1:
            print "You stayed in Joseon 'til you died."
            return 'death'

        elif a == 2:
            print "You were oppressed by the soldiers, and got imprisoned."
            print "You stayed in Joseon 'til you died."
            return 'death'

        elif a == 3:
            print "The mysterious room was the laser weapon armory."
            return 'laser_weapon_armory'
        else:
            print "One who cannot even type in the number is not qualified"
            print "to play this game."
            exit(0)


class LaserWeaponArmory(Scene):

    def enter(self):
        print "Here's the Laser Weapon Armory where"
        print "you can acquire a killing weapon."
        print "Suddenly you hear the footstep of the"
        print "soldiers outside the armory."
        print "Now the door is opening, and you see a gun on the table."
        print "In order to shoot, You hold up the gun."
        print "Whether it is a weapon or a toy will be depend on your luck."
        raw_input("\nPRESS ENTER TO CHECK YOUR LUCK")
        number = randint(1, 6)
        if number == 1:
            print "Bad luck. You shot the bb gun."
            print"You're arrested by the soldiers.\n"
            return 'death'
        if number == 2:
            print "Bang!"
            print "Well, your gun is a real one, but the soldiers"
            print "are equipped with bulletproof clothes."
            print "Soldier shot by you shot you back.\n"
            return 'death'
        if number == 3:
            print "Bang! Bang! Bang!"
            print "Out of Ammo\n"
            return 'death'
        if number == 4:
            print "Pew!"
            print "You chose a laser gun. You killed all the soldiers"
            return 'the_bridge'
        if number == 5:
            print "Pew!"
            print "You chose a laser gun. You killed all the soldiers"
            return 'the_bridge'
        if number == 6:
            print "Pew!"
            print "You chose a laser gun. You killed all the soldiers"
            return 'the_bridge'


class TheBridge(Scene):

    def enter(self):
        print "You've arrived to the bridge that leads to the escapepod."
        print "Suddenly, a giant aligator crawled out from the river"
        print "and stopped on the middle of the bridge."
        print "How will you go accross the bridge?"
        print "You have three choices (type the number)"
        print "1. Go back and stay in Joseon."
        print "2. Fight against the aligator."
        print "3. Go down to the river and swim."

        b = int(input("\n>>>"))

        if b == 1:
            print "You stayed in Joseon 'til you died."
            return 'death'
        elif b == 2:
            print "The aligator bit your hand."
            print "The aligator wasn't hungry."
            print "It said sorry and let you go."
            return 'escape_pod'
        elif b == 3:
            print "Obviously, the aligators were there.."
            return 'death'
        else:
            print "One who cannot even type in the number is not qualified"
            print "to play this game."
            exit(0)


class EscapePod(Scene):

    def enter(self):
        print "You're almost there! You're in the escapepod now."
        print "There are 3 pods in front of you."
        print "Type the number of your choice."
        print "1. first pod"
        print "2. second pod"
        print "3. third pod"

        c = int(input("\n>>>"))

        if c == 1:
            print "You've rode a ship to Japan"
            print "Another journey's waiting for you. :)"
            exit(0)
        elif c == 2:
            print "You've rode a ship to Netherland."
            print "Your family is waiting for you."
            print "Happy Ending"
            return 'ending'
        elif c == 3:
            print "The ship you rode sank in the middle of the sea."
            return 'death'
        else:
            print "One who cannot even type in the number is not qualified"
            print "to play this game."
            exit(0)


class Ending():

    def enter(self):
        print "Good work!"
        return 'ending'


class Map(object):

        # attribute lowercased with underscores
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'ending': Ending()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        ret = Map.scenes.get(scene_name)
        return ret

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()