from string import ascii_lowercase

file = open("day2/input.txt", "r")
boxes = file.read().splitlines()

cnt2 = 0
cnt3 = 0

for i in range(0, len(boxes)):
    box = str(boxes[i])
    hasTwoChars = False
    hasThreeChars = False
    for char in ascii_lowercase:
        if list(box).count(char) == 2:
            hasTwoChars = True
        if list(box).count(char) == 3:
            hasThreeChars = True   
    if hasTwoChars: cnt2 += 1
    if hasThreeChars: cnt3 += 1

final = cnt2 * cnt3
print(final)