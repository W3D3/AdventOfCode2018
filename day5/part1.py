file = open("day5/input.txt", "r")
polymer = list(file.read())

def react(c, n):
    return str(c).lower() == str(n).lower() and (str(c).islower() and str(n).isupper() or str(c).isupper() and str(n).islower())

i = 0
while i < len(polymer) - 1:
    currentUnit = polymer[i]
    nextUnit = polymer[i+1]
    # print(currentUnit, nextUnit)
    if react(currentUnit, nextUnit):
        # print(currentUnit, nextUnit, " reacted!")
        del(polymer[i])
        del(polymer[i])
        # print(polymer)
        i -= 1
    else:
        i += 1

print(''.join(polymer))
print(len(polymer))
