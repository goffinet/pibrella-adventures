## Basic (UK) Traffic Light Example
#
# When the Pibrella button is pressed, loop through the traffic light sequence.
# In the UK this is Red and Amber, Green, Amber, Red.

import pibrella, time

# Traffic light sequence, each light represents the red, amber and green light values and a time delay
sequence = [
    [1, 1, 0, 1],
    [0, 0, 1, 5],
    [0, 1, 0, 2],
    [1, 0, 0, 1]
]

# Callback function to process button presses
def button_changed(pin):
    if pin.read() == 1:
        traffic_light()

# Simple function to loop the traffic light sequence
def traffic_light():
    for i in sequence:
        pibrella.light.red.write(i[0])
        pibrella.light.yellow.write(i[1])
        pibrella.light.green.write(i[2])
        time.sleep(i[3])

# Set initial state (red light)
pibrella.light.red.on()

# Register the button press callback
pibrella.button.changed(button_changed)

# Wait for input
pibrella.pause()
