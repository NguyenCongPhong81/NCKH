from datetime import *
# Fomat date and time: Day/Month/year Hour:Minute
formatTime = "%d/%m/%Y %H:%M"
formatTimeStr = "%Y%m%d%H%M"

flightName = {}     # Create dictionary: { flight code : flight name }
flightGraph = {}    # Create dictionary: { depart-arrived : flights code }
flightTime = {}     # Create dictionary: { flight code : times }
flightRoute = {}    # Create dictionary: { depart : arriveds }

# Convert string to time
def t(time):
    return datetime.strptime(time, formatTime)

def tInt(time):
    return int(time.strftime(formatTimeStr))

def getFlightName(fileName):
    with open(fileName, "r") as file:
        for line in file:
            line = line[:-1:].split('\t')
            flightName.update({line[1] : line[0]})

def getFlightGraph(fileName):
    with open(fileName, "r") as file:
        for line in file:
            line = line.split()
            key = line[0]
            flightGraph.update({key : line[1:]})
            
            depart, arrival = key.split("-")
            if depart in flightRoute:
                flightRoute[depart].append(arrival)
            else:
                flightRoute.update({depart : [arrival]})

def getFlightTime(fileName):
    with open(fileName, "r") as file:
        for line in file:
            line = line.split()
            key = line[0]
            value = [[line[i] + ' ' + line[i+1], line[i+2] + ' ' + line[i+3]] for i in range(1, len(line)-3, 4)]
            flightTime.update({key : list(sorted(value, key = lambda x : t(x[1])))})

getFlightName("data\\flightName.txt")
getFlightGraph("data\\flightGraph.txt")
getFlightTime("data\\flightTime.txt")