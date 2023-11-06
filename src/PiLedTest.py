import socket
import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch
import version as ver

def main():
    led.init()
    switch.init()
    while True:
        if switch.read_slide_switch()== 1:
            led.set_output(0, 1)
            time.sleep(0.1)

            led.set_output(0, 0)
            time.sleep(0.1)
        else:
            startTime=time.time()
            while (time.time()-startTime<5):
                led.set_output(0, 1)
                time.sleep(0.05)

                led.set_output(0, 0)
                time.sleep(0.05)

            while switch.read_slide_switch()== 0:
                led.set_output(0,0)
    
    
    
if __name__ == "__main__":
    main()