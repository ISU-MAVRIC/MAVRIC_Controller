__author__ = 'Mark'

import pygame


pygame.init()
pygame.joystick.init()

clock = pygame.time.Clock()

joystick_count = pygame.joystick.get_count()
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    print("Joystick {}".format(i))
    print(joystick.get_name())

    axes = joystick.get_numaxes()
    print("Number of Axes: {}".format(axes))