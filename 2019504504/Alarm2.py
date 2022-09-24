import random
tt=50
while(1):
    temp=random.randrange(10,75)
    hum=random.randrange(0,80)
    al = "On" if tt < temp else "Off"
    print("Temperature: ",temp," Alarm: ",al)
