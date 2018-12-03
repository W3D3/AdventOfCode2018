file = open("day1/input.txt", "r")
nums = file.read().splitlines()

freq = 0
freqs = []
dupe = False
while dupe == False:
    for i in range(0, len(nums)):
        if str(nums[i][0]) == "+":
            freq = freq + int(nums[i][1:])
        if str(nums[i][0]) == "-":
            freq = freq - int(nums[i][1:])
        
        freqs.append(freq)
        if(freqs.count(freq) == 2):
            print(freq)
            exit()
print(freq)