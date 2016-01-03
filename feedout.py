import ledcontroller
import time

led = ledcontroller.LedController("10.0.0.5",pause_between_commands=0.1)



led.on(1)
led.white(1)
led.set_brightness(100,1)

for i in range(1,26):
    time.sleep(60)
    led.set_brightness((26-i)*4,1)

led.off(1)
