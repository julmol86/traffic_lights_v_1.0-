from machine import Pin
from time import sleep

red_B = Pin(13, Pin.OUT)
yellow_B = Pin(12, Pin.OUT)
green_B = Pin(15, Pin.OUT)

long = 4
normal = 2
short = 1

green_B.on()
yellow_B.on()
red_B.on()
sleep(short)
yellow_B.off()
red_B.off()
green_B.off()
sleep(short)
while True:
    green_B.on()
    sleep(long)
    green_B.off()
    yellow_B.on()
    sleep(normal)
    yellow_B.off()
    red_B.on()
    sleep(long)
    yellow_B.on()
    sleep(short)
    red_B.off()
    sleep(normal)
    yellow_B.off()

