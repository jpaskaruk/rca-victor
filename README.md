# rca-victor
new guts for an old classic

This is a fun work in progress, mostly intended as a demo of my non-ineptitude with Python, and comfort working with Unix, for potential employers.

My linkedin is at https://www.linkedin.com/in/james-paskaruk-a17737244/ if you want to hire me, for Python dev, IoT, or straight IT/DevOps roles.
You might also gather from the nature of this project that I'm interested in working on escape rooms, and you would be correct in that assumption.

My IMDB page is at https://www.imdb.com/name/nm8224891/
It currently does not reflect my most recent work on contract at Mikros Animation, where I worked on Thelma The Unicorn as a TD.
When I was at Tangent, I was a TD for the last two years with a strong focus on IaC and CI/CD processes, and the head IT guy for the Winnipeg office for the four years before that.

The project is a conversion of an old RCA Victor radio into an internet streaming radio, with a few escape room-style additions.

Basis of the new brains is a Raspberry Pi with a Hifiberry-style audio hat and three rotary encoders to manage the knobs:
Left knob will mute/unmute (Pi will run all the time and act as a redundant pi-hole server) and control volume.
Middle knob will be "tuning," which will crossfade into a static noise and then into the next "station". Demo here: https://www.youtube.com/watch?v=1zuO0uA6Jhw
Right knob will control a FLux Capacitor, which in practical terms means a low-pass filter for year of release - as you dial back, it plays only older and older things.

Also planned is a screen behind the tuning window which simulates a needle and does visual effects (ie. name of track/broadcast); this will also allow adding local radio stations' streams at their proper spot on the AM dial.

I used python-vlc to handle the audio mixing, it is the most simple way to manage multiple audio sources. I am assuming it will be just as easy to play a stream with it, which makes this mostly sorted, once I have tuning working both ways and a simple filter written.

I will be adding the OpenSCAD and stl files for the 3D printed parts I created to hold the knobs, they might already be there when you read this but they are not as I write this.
