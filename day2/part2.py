def hamdist(str1, str2):
#    """Count the # of differences between equal length strings str1 and str2"""
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                diffs += 1
    return diffs

def samechars(str1, str2):
    same = ""
    for ch1, ch2 in zip(str1, str2):
            if ch1 == ch2:
                same += ch1
    return same

file = open("day2/input.txt", "r")
boxes = file.read().splitlines()

for i in range(0, len(boxes)):
    for j in range(0, len(boxes)):
        if hamdist(boxes[i], boxes[j]) == 1:
            print(samechars(boxes[i], boxes[j]))
            exit()