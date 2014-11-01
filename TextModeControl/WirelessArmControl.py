__author__ = 'Mark'

import serial
import pygame


def main():
    pygame.init()
    pygame.joystick.init()

    clock = pygame.time.Clock()

    ser = serial.Serial('COM4', 57600); #Virtual Serial Port for now

    #print joystick info
    # joystick_count = pygame.joystick.get_count()
    # for i in range(joystick_count):
    #     joystick = pygame.joystick.Joystick(i)
    #     joystick.init()
    #     print("Joystick {}".format(i))
    #     print(joystick.get_name())
    #
    #     axes = joystick.get_numaxes()
    #     print("Number of Axes: {}".format(axes))

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    while True:
        clock.tick(100)
        pygame.event.pump()
        joyX = -joystick.get_axis(1)
        joyY = -joystick.get_axis(3)

        # print(leftJoyValue)
        # print(rightJoyValue)

        leftPower = int(mapRange(joyX, -1, 1, -127, 127))
        rightPower = int(mapRange(joyY, -1, 1, -127, 127))

        packet = "<{:0=+4d} {:0=+4d}>".format(leftPower, rightPower)

        ser.write(packet)
        print(packet)

        print(ser.readline())
        #print(ser.readline())




def mapRange(value, inMin, inMax, outMin, outMax):
    inRange = inMax - inMin
    outRange = outMax - outMin

    inPercentageOfRange = float(value - inMin)/float(inRange)

    return outMin + (inPercentageOfRange * outRange)

if __name__ == '__main__':main()