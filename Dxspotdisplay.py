# Demo program for the I2C 20x4 Display
# Created by IZ0FIU Max In Formia JN61TG

# Import necessary libraries for communication and display use
from RPLCD.i2c import CharLCD
import time
import getpass
import sys
import telnetlib

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

tn = telnetlib.Telnet('node address', port) #please enter DX Cluster address and port node
tn.read_until(b"login: ")
tn.write('your callsign' + "\n") #please enter your callsign
time.sleep(5)

# Main body of code
try:
    while True:
        line = tn.read_until("\n")  # Read one line
        l1 = line.split()
        add = [" "," "," "," "," "," "," "," "," "," "]
        l1.extend(add)

        print(l1)[0],(l1)[1],(l1)[2],(l1)[3],(l1)[4],(l1)[5],(l1)[6],(l1)[7],(l1)[8]
        lcd.write_string((l1)[0])
        lcd.write_string(" "+(l1)[1])
        lcd.write_string(" "+(l1)[2])
        lcd.cursor_pos = (1, 0)
        lcd.write_string((l1)[3])
        lcd.write_string(" "+(l1)[4])
        lcd.cursor_pos = (2, 0)
        lcd.write_string((l1)[5])
        lcd.write_string(" "+(l1)[6])
        time.sleep(10)  #i add time between spot. If you want different seconds, change 10
        lcd.close(clear=True)

        if b'abcd' in line:  # last line, no more read
            break
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the pr$
    print("Cleaning up!")
    lcd.close(clear=True)


