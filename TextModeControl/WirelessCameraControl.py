__author__ = 'Mark'

import serial
import pygame


def main():
    pygame.init()
    pygame.joystick.init()

    clock = pygame.time.Clock()

    ser = serial.Serial('COM5', 57600);

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
        clock.tick(10)
        pygame.event.pump()
        joyX = -joystick.get_axis(1)
        joyY = -joystick.get_axis(0)

        # print(leftJoyValue)
        # print(rightJoyValue)

        tiltspeed = int(mapRange(joyX, -1, 1, -3, 2))
        panspeed = int(mapRange(joyY, -1, 1, -3, 2))

        packet = "<{:0=+4d} {:0=+4d}>".format(tiltspeed, panspeed)

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