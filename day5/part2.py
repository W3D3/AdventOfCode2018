def react(c, n):
    return str(c).lower() == str(n).lower() and (str(c).islower() and str(n).isupper() or str(c).isupper() and str(n).islower())

def fullReact(poly):
    polymer = poly.copy()
    i = 0
    while i < len(polymer) - 1:
        currentUnit = polymer[i]
        nextUnit = polymer[i+1]
        # print(currentUnit, nextUnit)
        if react(currentUnit, nextUnit):
            #print(currentUnit, nextUnit, " reacted!")
            del(polymer[i])
            del(polymer[i])
            # print(polymer)
            i -= 1
        else:
            i += 1
    return polymer

from string import ascii_lowercase
file = open("day5/input.txt", "r")
polymer = list(file.read())

minReducedSize = float("inf")
for char in ascii_lowercase:
    newpolymer = [x for x in polymer if str(x) != char and str(x) != char.upper()] #list(filter(lambda c: c != char, polymer))
    if len(newpolymer) < len(polymer):
        #print(newpolymer)
        result = fullReact(newpolymer)
        if(len(result) < minReducedSize):
            minReducedSize = len(result)

print(minReducedSize)
