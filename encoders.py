from threading import Event
from queue import Queue
from gpiozero import RotaryEncoder, Button
import alsaaudio

# pins connected to KY040 rotary encoders
rotor3 = RotaryEncoder(15,14)
rotor2 = RotaryEncoder(24,23)
rotor1 = RotaryEncoder(8,25)
btn3 = Button(17, pull_up=True)
btn2 = Button(27, pull_up=True)
btn1 = Button(7, pull_up=True)
# Event object
done = Event()
# alsa mixer object for setting volume
mixer = alsaaudio.Mixer()
mixer.setvolume(75)

vol_stash = Queue()

def adjustvolup():
    current = mixer.getvolume()[0]
    newvol = current + 1
    mixer.setvolume(newvol)

def adjustvoldown():
    current = mixer.getvolume()[0]
    newvol = current - 1
    mixer.setvolume(newvol)

def mute():
    current = mixer.getvolume()[0]
    vol_stash.put(current)
    mixer.setvolume(0)

def unmute():
    stashed_vol = vol_stash.get()
    mixer.setvolume(stashed_vol)

def togglemute():
    if vol_stash.empty():
        mute()
    else:
        unmute()

def clockw():
    print("clockwise!")

def counterw():
    print("counterclockwise!")

def pus():
    print("pushed!")

# Knob 1
rotor1.when_rotated_clockwise = adjustvolup
rotor1.when_rotated_counter_clockwise = adjustvoldown
btn1.when_released = togglemute

done.wait()
