# Import function get flight name, flight time, flight code
# Import function convert string to time: t(time)
from readFile import *  

timeINFINITY = tInt(datetime(9999, 12, 31))
timeStrInfinity = "31/12/9999 23:59"
waitingTime = 30

def choseFlight(Depart, Arrival, startTime):
    # Initialize return value
    airPlaneCode = None; timeDepart = timeStrInfinity; timeArrival = timeStrInfinity

    timeDifference = timeINFINITY

    flightNumbers = flightGraph[Depart + "-" + Arrival]

    for flightNumber in flightNumbers:
        Times = flightTime[flightNumber]
        for Time in Times:
            timeDelta = tInt(t(Time[1])) - tInt(t(startTime))
            if timeDelta > timeDifference:
                break

            if tInt(t(Time[0])) >= tInt(t(startTime)) + waitingTime:
                timeDifference = timeDelta
                timeDepart = Time[0]
                timeArrival = Time[1]
                airPlaneCode = flightNumber

    return airPlaneCode, timeDepart, timeArrival