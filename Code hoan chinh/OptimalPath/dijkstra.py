from chose import *

class node:
    def __init__(self, name, airPlaneCode, timeDepart, timeArrival, prev):
        self.name = name                    # string
        self.airPlaneCode = airPlaneCode    # string
        self.timeDepart = timeDepart        # string
        self.timeArrival = timeArrival      # string
        self.prev = prev                    # string

nodes = {} # Create dictionary save node

def days_hours_minutes(td):
    return f'days = {td.days}, hours = {td.seconds//3600}, minutes = {(td.seconds//60)%60}'

# Recovery path
def path(start, end):
    result = []; temp = end
    while temp != start:
        result.append(nodes[temp].prev + " → " + nodes[temp].name + " " + flightName[nodes[temp].airPlaneCode] + ": " + nodes[temp].timeDepart + " " + nodes[temp].timeArrival)
        temp = nodes[temp].prev
    return list(reversed(result))

# Algorithm dijkstra (file, start, end)
def dijkstra(start, end, d, m, y, h, mn):
    start = start.strip().upper()
    end = end.strip().upper()
    d = d.strip()
    m = m.strip()
    y = y.strip()
    h = h.strip()
    mn = mn.strip()
    startTime = d + '/' + m + '/' + y + ' ' + h + ':' + mn

    V = list(flightRoute.keys())
    T = V.copy()

    if start not in V:
        return timeINFINITY, ['Start is not in the graph']
    if end not in V:
        return timeINFINITY, ['End is not in the graph']

    for name in V:
        nodes.update({name : node(name, None, timeStrInfinity, timeStrInfinity, None)})
    
    nodes[start].timeDepart = startTime
    nodes[start].timeArrival = startTime

    while True:
        i = min(T, key = lambda x: tInt(t(nodes[x].timeArrival)))
        T.remove(i)

        if end not in T or i == end:
            break

        for k in flightRoute[i]:
            if k not in T:  continue

            airPlaneCode, timeDepart, timeArrival = choseFlight(i, k, nodes[i].timeArrival)
            if tInt(t(nodes[k].timeArrival)) > tInt(t(timeArrival)):
                nodes[k].airPlaneCode = airPlaneCode
                nodes[k].timeDepart = timeDepart
                nodes[k].timeArrival = timeArrival
                nodes[k].prev = i

    # return length, path
    if nodes[end].timeArrival == timeStrInfinity:
        return timeINFINITY, ["The path does not exist"]
    else:
        return days_hours_minutes(t(nodes[end].timeArrival) - t(nodes[start].timeDepart)), path(start, end)