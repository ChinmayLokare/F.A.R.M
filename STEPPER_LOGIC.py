from time import sleep
import RPi.GPIO as GPIO
DIR =12
STEP =5
CW = 1
CCW = 0
EN=7
#M0=8
#M1=11
#M2=25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN,GPIO.OUT)
#GPIO.setup(M0,GPIO.OUT)
#GPIO.setup(M1,GPIO.OUT)
#GPIO.setup(M2,GPIO.OUT)
GPIO.setup(DIR,GPIO.OUT)
GPIO.setup(STEP,GPIO.OUT)
GPIO.output(EN,GPIO.HIGH)
GPIO.output(DIR,GPIO.HIGH)
delay=0.0005
#GPIO.output(M0,GPIO.LOW)
#GPIO.output(M1,GPIO.LOW)
#GPIO.output(M2,GPIO.LOW)
GPIO.output(EN, GPIO.LOW)
while(1):
 angle=input(' enter angle ')
 print(angle)
 #step_count=float((angle)/(1.8))
 #print(round(step_count))
 #step_count=round(step_count)
 #step_count=int(step_count)
 #print(step_count)
 if angle > 0:
  step_count=float((angle)/(1.8))
  print(round(step_count))
  step_count=round(step_count)
  step_count=int(step_count)
  print(step_count)
  step_count=step_count
  for x in range(step_count):
   GPIO.output(EN,GPIO.LOW)
   GPIO.output(DIR,GPIO.LOW)
   print('CLOCKWISE')
   GPIO.output(STEP,GPIO.HIGH)
   print('clockwise high')
   sleep(delay)
   GPIO.output(STEP,GPIO.LOW)
   print('clockwise low')
   sleep(delay)
  sleep(0.05)

 elif angle < 0:
  angle=angle*(-1)
  A_step_count=((angle)/(1.8))
  print(round(A_step_count))
  A_step_count=round(A_step_count)
  A_step_count=int(A_step_count)
  A_step_count=A_step_count
  print(A_step_count)
  for x in range(A_step_count):
   GPIO.output(DIR, GPIO.HIGH)
   GPIO.output(EN,GPIO.LOW)
   print('ANTI-CLOCKWISE')
   GPIO.output(STEP,GPIO.HIGH)
   print('Anticlockwise high')
   sleep(delay)
   GPIO.output(STEP,GPIO.LOW)
   print('Anticlockwise low')
   sleep(delay)
  sleep(0.05)
GPIO.output(EN,GPIO.HIGH)
GPIO.cleanup()



