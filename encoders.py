from threading import Event
from gpiozero import RotaryEncoder, Button

rotor1 = RotaryEncoder(15,14)
rotor2 = RotaryEncoder(24,23)
rotor3 = RotaryEncoder(8,25)
btn1 = Button(17, pull_up=True)
btn2 = Button(27, pull_up=True)
btn3 = Button(7, pull_up=True)
done = Event()

def clockw():
    print("clockwise!")

def counterw():
    print("counterclockwise!")

def pus():
    print("pushed!")

for rotor in [rotor1,rotor2,rotor3]:
    rotor.when_rotated_clockwise = clockw
    rotor.when_rotated_counter_clockwise = counterw

for btn in [btn1,btn2,btn3]:
    btn.when_released = pus

done.wait()
