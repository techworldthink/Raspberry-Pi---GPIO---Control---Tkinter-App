import time
import RPi.GPIO as GPIO
from datetime import datetime
from datetime import date

pins_state = [0,0,0,0,0]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.setmode (GPIO.BOARD)


for pins in range(5):
    GPIO.setup(pins, GPIO.IN)
                
while(True):
    try:
        for pin in range(5):
            pin_satte_now = GPIO.input(pin)
            if(pin_satte_now != pins_state[pin]):
            #if(pin_satte_now):
                    
                print("pin "+str(pin)+" state "+str(pins_state[pin])+" -> "+str(pin_satte_now))
                pins_state[pin]=pin_satte_now
                today = date.today()
                d1 = today.strftime("%d/%m/%Y")
                print("d1 =", d1)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("Current Time =", current_time)
                print("\n\n")
                """else:
                    
                    print("pin "+str(pin)+" state "+str(pins_state[pin])+" -> "+str(GPIO.input(pin)))
                    pins_state[pin]=GPIO.input(pin)
                    today = date.today()
                    d1 = today.strftime("%d/%m/%Y")
                    print("d1 =", d1)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("Current Time =", current_time)
                    print("\n\n")"""
    except Exception as e:
        print("Error")
        print(e)
        time.sleep(5)
    finally:
        time.sleep(1)


