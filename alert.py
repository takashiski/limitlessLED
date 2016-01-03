import ledcontroller
import time

led = ledcontroller.LedController("10.0.0.5",pause_between_commands=0.05);


led.on(1)
led.white(1)
led.off(1)
led.on(1)
led.off(1)
led.on(1)
led.off(1)
led.on(1)
led.white(1)

