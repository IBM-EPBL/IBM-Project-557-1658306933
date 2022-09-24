# Imports
import random
high_temp = 60 # Threshold for high temperature
while True: # Continuously generate temperature and humidity
    temp = random.randrange(20, 81) # Temperature between 20'C and 80'C
    humidity = random.randrange(0, 101) # Humidity
    if temp > high_temp:
        alarm = 'on'
    else:
        alarm = 'off'
    print('Alarm: ', alarm)