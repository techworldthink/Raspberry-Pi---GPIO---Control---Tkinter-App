import time
import RPi.GPIO as GPIO
from datetime import datetime
from datetime import date

pins_state = [0,0,0,0,0]

while(True):
    try:
        for pin in range(5):
            if(GPIO.input(pin) != pins_state[pin]):
                if(GPIO.input(pin)):
                    pins_state[pin]=1
                    print("pin "+str(pin)+"state "+str(pins_state[pin])+" -> "+str(GPIO.input(pin)))
                    today = date.today()
                    d1 = today.strftime("%d/%m/%Y")
                    print("d1 =", d1)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("Current Time =", current_time)
                    print("\n\n")
                else:
                    pins_state[pin]=0
                    print("pin "+str(pin)+"state "+str(pins_state[pin])+" -> "+str(GPIO.input(pin)))
                    today = date.today()
                    d1 = today.strftime("%d/%m/%Y")
                    print("d1 =", d1)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("Current Time =", current_time)
                    print("\n\n")
    except:
        time.sleep(5)
    finally:
        time.sleep(1)


