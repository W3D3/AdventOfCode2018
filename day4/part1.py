from datetime import datetime
from operator import attrgetter

class Entry:
    def __init__(self, time, event):
        # [1518-06-05 00:46] falls asleep
        self.time = datetime.strptime(time, '%Y-%m-%d %H:%M')
        self.event = event

    def isShiftChange(self):
        return str(self.event).count("begins shift") >= 1

    def fellAsleep(self):
        return self.event == "falls asleep"

    def wokeUp(self):
        return self.event == "wakes up"

    def getMinute(self):
        return self.time.minute

    def getDate(self):
        return str(self.time.isoformat().split("T")[0])

    def getGuardId(self):
        if self.isShiftChange == False: 
            return 0
        return int(str(self.event).replace("Guard #", "").replace(" begins shift", ""))

    def print(self):
        print(self.time, self.event)

class Guard:
    def __init__(self, id):
        self.id = id
        self.hours = dict()
        #self.hour = [0 for x in range(60)]

    def setSleep(self, date, asleep, awake):
        if date not in self.hours:
            self.hours[date] = [0 for x in range(60)]
        for i in range(asleep, awake):
            self.hours[date][i] = 1

    def getSleepMinutes(self):
        sleep = 0
        for k, hour in self.hours.items():
            for i in range(0, len(hour)):
                sleep += hour[i]
        return sleep

    def getSleepyness(self):
        sleepyness = [0 for x in range(60)]
        for k, hour in self.hours.items():
            for i in range(0, len(hour)):
                sleepyness[i] += hour[i]
        return sleepyness

    def print(self):
        print("Guard #", self.id, ": Sleeptime: ", self.getSleepMinutes(), end = "\n")
        for date, hour in self.hours.items():
            print("[", date, "]", end = "")
            for i in range(0, len(hour)):
                print("#" if hour[i] == 1 else ".", end = "")
            print("")

file = open("day4/input.txt", "r")
log = file.read().splitlines()
entries = list()

for i in range(0, len(log)):
    arr = str(log[i]).split("] ")
    date = arr[0].lstrip('[')
    text = ''.join(arr[1:])

    e = Entry(date, text)
    entries.append(e)

entries.sort(key = attrgetter('time'), reverse = False)

guards = dict()
for i in range(0, len(entries)):
    #entries[i].print()
    if entries[i].isShiftChange():
        id = entries[i].getGuardId()
    elif entries[i].fellAsleep():
        start = entries[i].getMinute()
    elif entries[i].wokeUp():
        end = entries[i].getMinute()

        if str(id) in guards:
            guards[str(id)].setSleep(entries[i].getDate(), start, end)
        else:
            guards[str(id)] = Guard(id)
            guards[str(id)].setSleep(entries[i].getDate(), start, end)

maxsleep = 0
maxg = None
for x, g in guards.items():
  #g.print()
  if g.getSleepMinutes() > maxsleep:
      maxsleep = g.getSleepMinutes()
      maxg = g

print("Maximum sleep guard:")
maxg.print()

indexOfSleepyDay = maxg.getSleepyness().index(max(maxg.getSleepyness()))
print(maxg.getSleepyness())
print("Sleepiest in minute: ", indexOfSleepyDay)
print("Minute * ID = ", indexOfSleepyDay * maxg.id)