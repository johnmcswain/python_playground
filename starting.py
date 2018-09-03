print("Hello World")
myarray = []
myarray.append("Yes")
myarray.append("No")
print(myarray)
print("more money? %s; more problems? %s" % (myarray[0],myarray[1]))

for x in myarray:
    print(x)


def primeNumbers(x):
    for val in range(2,x-1):
        if x % val != 0:
            return True
        else:
            return False
    return x > 1

print(primeNumbers(7451))

class SuperHero:
    name = None
    age = None
    power = None
    def destroyAPlanet(self):
        print("planet has been destroyed by %s, aka" % (self.name, debug(self)))

greenLantern = SuperHero()
greenLantern.name = "John Smith"
greenLantern.age = 34
greenLantern.destroyAPlanet();