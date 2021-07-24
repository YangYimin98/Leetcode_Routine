def efficientCabScheduling(n, cabTripTime):
    if len(cabTripTime) == 1:
        return n * cabTripTime[0]
    else:
        trips, time = 0, 0
        while trips < n:
            time += 1
            for i in cabTripTime:
                if time % i == 0:
                    trips += 1
        return time
