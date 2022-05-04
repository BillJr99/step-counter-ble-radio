def on_received_number(receivedNumber):
    global otherstep
    otherstep = receivedNumber
    basic.show_icon(IconNames.SCISSORS)
    basic.pause(100)
    basic.show_number(radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH))
    basic.pause(500)
radio.on_received_number(on_received_number)

def on_gesture_shake():
    global step
    step += 1
    radio.send_number(step)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

otherstep = 0
step = 0
step = 0
otherstep = 0
radio.set_group(1)

def on_forever():
    basic.show_icon(IconNames.STICK_FIGURE)
    basic.show_number(step)
    basic.pause(100)
    basic.show_icon(IconNames.HEART)
    basic.pause(100)
    basic.show_number(otherstep)
    basic.pause(100)
    led.stop_animation()
basic.forever(on_forever)
