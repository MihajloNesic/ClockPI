
import pifacecad as p
import time
import datetime
from datetime import timedelta

now = datetime.date.today()
day = now.day
month = now.month
year = now.year

v=str(day)+"."+str(month)+"."+str(year)

print(now)
print(v)

cad = p.PiFaceCAD()
cad.lcd.clear()
cad.lcd.backlight_on()
cad.lcd.blink_off()
cad.lcd.cursor_off()

while True:
        cad.lcd.write(time.strftime("%H:%M:%S"))
        cad.lcd.set_cursor(0, 1)
        #cad.lcd.write(str(now))
        now = datetime.date.today()
        v=str(now.day)+"."+str(now.month)+"."+str(now.year)
        cad.lcd.write(v)
        cad.lcd.set_cursor(0, 0)
        time.sleep(0.9)
        cad.lcd.clear()
