from string import ascii_uppercase

class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = int(x)
        self.y = int(y)

    def manDist(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def readableId(self):
        return str(chr(self.id + 65))
        # if (self.id < len(ascii_uppercase)):
        #     return ascii_uppercase[self.id]
        # else:
        #     return str(chr(self.id))

    def __str__(self):
        return self.readableId()

    # def __str__(self):
    #     return "["+ self.readableId() + "] (" + str(self.x) + ", " + str(self.y) + ")"

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

area = [0 for a in range(len(points))]
for y in range(0, maxY):
    for x in range(0, maxX):
        minDist = float("inf")
        for p in points:
            distance = p.manDist(x, y)
            if distance == 0:
                minDist = distance
                coords[x][y] = p
                break
            elif distance < minDist:
                minDist = distance
                coords[x][y] = p
            elif distance == minDist:
                coords[x][y] = "."

for y in range(0, maxY):
    for x in range(0, maxX):
        try:
            area[coords[x][y].id] += 1
        except:
            pass
       
# kill infinite areas
for y in range(0, maxY):
    for x in range(0, maxX):
        if(x == 0 or y == 0 or x == maxX or y == maxY):
            try:
                area[coords[x][y].id] = 0
            except:
                pass

printCoords(coords) 
print(max(area))