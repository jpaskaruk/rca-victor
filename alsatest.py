import alsaaudio

mx = alsaaudio.Mixer()
vol = mx.getvolume()
print(vol[0])
