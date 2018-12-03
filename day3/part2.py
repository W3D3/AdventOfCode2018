from string import ascii_lowercase

file = open("day3/input.txt", "r")
claims = file.read().splitlines()

w, h = 1000, 1000
fabric = [[0 for x in range(w)] for y in range(h)] 

for i in range(0, len(claims)):
    arr = str(claims[i]).split(" @ ")
    id = int(str(arr[0])[1:])
    data = arr[1].split(": ")
    coords = list(map(int, data[0].split(",")))
    size = list(map(int, data[1].split("x")))

    # print(id, " coords: ", coords, "size: ", size)
    for x in range(coords[0], coords[0]+size[0]):
        for y in range(coords[1], coords[1]+size[1]):
            fabric[x][y] += 1;

for i in range(0, len(claims)):
    arr = str(claims[i]).split(" @ ")
    id = int(str(arr[0])[1:])
    data = arr[1].split(": ")
    coords = list(map(int, data[0].split(",")))
    size = list(map(int, data[1].split("x")))

    untouched = True;
    # print(id, " coords: ", coords, "size: ", size)
    for x in range(coords[0], coords[0]+size[0]):
        for y in range(coords[1], coords[1]+size[1]):
            if fabric[x][y] > 1: untouched = False
    if untouched:
        print(id)
        exit()