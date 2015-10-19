import pygame, sys, os, serial, time
from pygame.locals import *
  
def quit():
    pygame.quit()
    ser.close()
    sys.exit(0)
  
def input(events):
    deadzone = 0.5
    for event in events:
        if event.type == QUIT:
            quit()
        else:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
            elif event.type == JOYAXISMOTION and abs(event.value) > deadzone:
                if event.axis == 1:
                    if event.value < 0:
                        ser.write("0")
                    else:
                        ser.write("1")
                elif event.axis == 0:
                    if event.value > 0:
                        ser.write("2")
                    else:
                        ser.write("3")
                print event
            elif event.type != JOYAXISMOTION and event.type != MOUSEMOTION:
                print event

try:
    ser = serial.Serial()
    ser.port = 2
    ser.baudrate = 9600
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.stopbits = serial.STOPBITS_ONE

    ser.open() # open first serial port
#    print ser.portstr  # check which port was really used

#   print ser.write(chr(0x80)+chr(0x10)+chr(0xF0)+chr(0x01)+chr(0xBF)+chr(0x40))
#   print ser.write("\x01\x03\x00\x00\x00\x01\x0a\x84")
except Exception as e:
    print(e)



pygame.init()
pygame.joystick.init()

# Set the display's dimensions
screenDimensions = (800, 600)
window = pygame.display.set_mode(screenDimensions)
pygame.display.set_caption('MAVRIC Test') # Set the window bar title
screen = pygame.display.get_surface() # This is where images are displayed
  
# Clear the background
background = pygame.Surface(screen.get_size()).convert()
background.fill((255, 255, 255))
screen.blit(background, (0,0))
  
# Draw a string onto screen
font = pygame.font.Font(None, 36)
text = font.render("MAVRIC Joystick Test", 1, (0, 0, 0))
screen.blit(text, (500, 400))
pygame.display.flip()

# Detect if joystick is available
joysticks = pygame.joystick.get_count()
if joysticks:
    print str(joysticks) + " joystick(s) detected!"
  
# Initialize each joystick
    for i in range(joysticks):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        name = joystick.get_name()
        print "Joystick " + str(i) + " name: " + name
  
# The game loop
while True:
    input(pygame.event.get())
  
