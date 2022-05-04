radio.onReceivedNumber(function (receivedNumber) {
    otherstep = receivedNumber
    basic.showIcon(IconNames.Scissors)
    basic.pause(100)
    basic.showNumber(radio.receivedPacket(RadioPacketProperty.SignalStrength))
    basic.pause(500)
})
input.onGesture(Gesture.Shake, function () {
    step += 1
    radio.sendNumber(step)
})
let otherstep = 0
let step = 0
step = 0
otherstep = 0
radio.setGroup(1)
basic.forever(function () {
    basic.showIcon(IconNames.StickFigure)
    basic.showNumber(step)
    basic.pause(100)
    basic.showIcon(IconNames.Heart)
    basic.pause(100)
    basic.showNumber(otherstep)
    basic.pause(100)
    led.stopAnimation()
})
