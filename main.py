import machine
from ACM1602NI import ACM1602NI
import time

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=50000)

lcd = ACM1602NI(i2c)

lcd.init()
lcd.lcd_clear()
lcd.write_lcd("Hello World!")
lcd.localte(0,1)
lcd.write_lcd("Raspberry Pi")
lcd.lcd_home()
