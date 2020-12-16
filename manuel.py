import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)
 
ajoutAngle = 5
print("ok")
pwm=GPIO.PWM(17,100)
pwm.start(5)
 
angle1 = 80
duty1 = float(angle1)/10 + ajoutAngle
 
angle2=180
duty2= float(angle2)/10 + ajoutAngle
 
pwm.ChangeDutyCycle(duty1)
time.sleep(1)
pwm.ChangeDutyCycle(duty2)
time.sleep(1)
GPIO.cleanup() 
