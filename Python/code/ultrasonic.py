import RPi.GPIO as GPIO
from time import sleep,time

SETTLE_TIME = 2
CALIBRATIONS = 5
CALIBRATION_DELAY = 1
TRIGGER_TIME = 0.0001
SPEED_OF_SOUND = 343 # meters per sec

GPIO.setmode(GPIO.BCM)

TRIG = 18
ECHO = 27

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# THe calibration function
def calibrate():
    print('Calibrating........')
    print('Place and object at a known distance away from the sensor')
    known_distance = float(input('Enter the distance'))

    print('Getting calibration measurements...')
    average_distance = 0
    for i in range(0, CALIBRATIONS):
        distance = getDistance()
        average_distance += distance
        sleep(CALIBRATION_DELAY)
    average_distance = average_distance / CALIBRATIONS

    correction_factor = known_distance / average_distance
    print('The correction factor is: ' ,correction_factor)
    print('Done calibrating.....')
    return correction_factor

# use the sensor to calcuate the distance to an object
def getDistance():
    GPIO.output(TRIG, GPIO.HIGG)
    sleep(TRIGGER_TIME)
    GPIO.output(TRIG, GPIO.LOW)

    # wait fo the echo pin to read high
    while(GPIO.input(ECHO) == GPIO.LOW):
        start = time()
    while(GPIO.input(ECHO) == GPIO.HIGH):
        end = time()
    duration = end - start
    distance = SPEED_OF_SOUND * duration
    distance = distance / 2
    distance *= 100
    return distance
# Main
print('Waiting for sensor to settle')
GPIO.output(TRIG, GPIO.LOW)
sleep(SETTLE_TIME)

correction_factor = calibrate()
print('Start Measuring the distance')
input('Press Enter to continue')

while(True):
    print("Measuring distance now.....")
    distance = getDistance() * correction_factor
    sleep(SETTLE_TIME)

    print('Distance measured is: {}'.format(distance))

    i = input('Get another measurement (Y/N)  ')

    if (i == 'N' or i == 'n'):
        break

print('Done')

# Cleanup the pins
GPIO.cleanup()



