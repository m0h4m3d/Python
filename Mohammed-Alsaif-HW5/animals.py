


class Animal:
    __name = ""
    def __init__(self, name):
        self.__name = name

    def guess_who_am_i(self):
        print("I will give you 3 hints, guess what animal I am")
        print()
        print()
        if(self.__name == "elephant"):
            print("I have exceptional memory")
            val = input("Who am i?: ")
            if(val == self.__name):
                print("You got it! I am "+val)
                return
            else:
                print("Nope, try again!")
            print()
            print()
            print("I am the largest land-living mammal in the world")
            val = input("Who am i?: ")
            if(val == self.__name):
                print("You got it! I am "+val)
                return
            else:
                print("Nope, try again!")
            print()
            print()
            print("I have two large teeth and trunck")
            val = input("Who am i?: ")
            if(val == self.__name):
                print("You got it! I am "+val)
                return
            else:
                print("Nope, try again!")
            print("I'm out of hints! The answer is: "+self.__name)
            return
        elif(self.__name == "tiger"):
            print("I am the biggest cat")
            val = input("Who am i?: ")
            if(val == self.__name):
                print("You got it! I am "+val)
                return
            else:
                print("Nope, try again!")
            print()
            print()
            print("I come in black and white or orange and black")
            val = input("Who am i?: ")
            if(val == self.__name):
                print("You got it! I am "+val)
                return
            else:
                print("Nope, try again!")
            print()
            print()
            print("I have two large teeth and trunck")
            val = input("Who am i?: ")
            if(val == self.__name):
                print("You got it! I am "+val)
                return
            else:
                print("Nope, try again!")
            print("I'm out of hints! The answer is: "+self.__name)
            return
        elif(self.__name == "bat"):
            print("I use echo-location")
            val = input("Who am i?: ")
            if(val == self.__name):
                print("You got it! I am "+val)
                return
            else:
                print("Nope, try again!")
            print()
            print()
            print("I can fly")
            val = input("Who am i?: ")
            if(val == self.__name):
                print("You got it! I am "+val)
                return
            else:
                print("Nope, try again!")
            print()
            print()
            print("I see well in dark")
            val = input("Who am i?: ")
            if(val == self.__name):
                print("You got it! I am "+val)
                return
            else:
                print("Nope, try again!")
            print("I'm out of hints! The answer is: "+self.__name)
            return



e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
