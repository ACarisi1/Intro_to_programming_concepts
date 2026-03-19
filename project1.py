
def avgRain(total_rain, count):
    return total_rain / count

def avgWind(total_wind, count):
    return total_wind / count

total_rain = 0.0
total_wind = 0.0
count = 0
rain, wind = map(float, input().split())
while rain != -1.0:
    total_rain += rain
    total_wind += wind
    count += 1
    line = input().split()
    if len(line) == 1:
        rain = float(line[0])
        wind = 0.0
    else:
        rain, wind = map(float, line)
if count > 0 :
    avg_r = avgRain(total_rain, count)
    avg_w = avgWind(total_wind, count)
    severity = (avg_r * 10) +avg_w
    print("Average rain is", round(avg_r,1), "inches")
    print("Average wind is", avg_w, "MPH")
    print("The weather for ", count, "severity is", severity)
else:
    print("No Data Entered")
