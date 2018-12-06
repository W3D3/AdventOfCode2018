from string import ascii_uppercase

class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = int(x)
        self.y = int(y)

    def manDist(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

def printCoords(coords):
    for y in range(0, len(coords[0])):
        for x in range(0, len(coords)):
            print(coords[x][y], end="")
        print()
    print()

file = open("day6/input.txt", "r")
inputCoords = file.read().splitlines()

maxX = 0
maxY = 0
points = list()
for i in range(0, len(inputCoords)):
    arr = str(inputCoords[i]).split(", ")
    point = Point(i , arr[0], arr[1])
    if point.x > maxX:
        maxX = point.x
    if point.y > maxY:
        maxY = point.y
    points.append(point)
maxX += 1
maxY += 1
coords = [["." for y in range(maxY)] for x in range(maxX)] 

maxTotalDistance = 10000
area = 0
for y in range(0, maxY):
    for x in range(0, maxX):
        sumDist = 0
        for p in points:
            sumDist += p.manDist(x, y)
        if sumDist < maxTotalDistance:
            coords[x][y] = "#"
            area += 1
       

printCoords(coords) 
print(area)