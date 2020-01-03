from gpiozero import LED
from gpiozero import MotionSensor

#Define which GPIO PIN slots are being used for the sensors/lights
green_led = LED(17) #GPIO pin 17, plugged into the slot BELOW the LONG end of the LED lead.  
pir = MotionSensor(4)
green_led.off()

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    green_led.on()
    pir.wait_for_no_motion()
    green_led.off()
    print("Motion Stopped")
    
#MotionSensor triggering Piezo Buzzer, integrated Arduino to RP4 with periphrials.  
    
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23. GPIO.IN) #PIR sensorGPIO 11(SCLK)
GPIO.setup(24. GPIO.IN) #Buzzer, GPIO 8(CEO)

try: 
    time.sleep(2) #to stablize sensor to start
    
    while True:
        if GPIO.input(23):
            GPIO.output(24, True)
            time.sleep(0.5) #Buzzer turns off for 0.5 sec
            GPIO.output(24, False)
            print ("Motion Detected...")
            time.sleep(5) #To avoid multiple detections
        time.sleep(0.1) #loop delay, should be less than detection delay
        
except:
    GPIO.cleanup()
