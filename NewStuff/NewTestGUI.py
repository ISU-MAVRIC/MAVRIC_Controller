'''
This program creates MAVRICS GUI where status of the Joysticks & of the Rover will be seen. 
Also this UI will be able to move the rover to any position by setting different input boxes with a respective box.
To be updated, currently it only handles joysticks position.
        to add 
                Wheels speed & position
                Arm position
'''
import sys
import pygame

pygame.init()

#Clock
clk = pygame.time.Clock()

#Read Joysticks
if pygame.joystick.get_count() == 0:
    raise IOError("No Joysticks Detected")
Leftjoy = pygame.joystick.Joystick(0)
Rightjoy = pygame.joystick.Joystick(1)
Leftjoy.init()
Rightjoy.init()

#Create display
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MAVRIC UI")

#Frame for Crosshairs zone
frame = pygame.Rect((45, 45), (200, 200))


#Crosshairs for left & right joysticks
#Left Crosshairs
Leftcrosshair = pygame.surface.Surface((10, 10))
Leftcrosshair.fill(pygame.Color("magenta"))
pygame.draw.circle(Leftcrosshair, pygame.Color("blue"), (5,5), 5, 0)
Leftcrosshair.set_colorkey(pygame.Color("magenta"), pygame.RLEACCEL)
Leftcrosshair = Leftcrosshair.convert()
#Right Crosshairs
Rightcrosshair = pygame.surface.Surface((10, 10))
Rightcrosshair.fill(pygame.Color("red"))
pygame.draw.circle(Rightcrosshair, pygame.Color("pink"), (5,5), 5, 0)
Rightcrosshair.set_colorkey(pygame.Color("red"), pygame.RLEACCEL)
Rightcrosshair = Rightcrosshair.convert()
'''
#MAVRIC widget
    #wheels
        #Front Left Wheel
surf = pygame.Surface((20,20))
surf.fill(pygame.Color("white"))
surf.set_colorkey(pygame.Color("white"))

pygame.draw.rect(surf, (100, 0, 0))

point = 200, 10

blittedRect = screen.blit(surf, point)
oldCenter = blittedRect.center
rotatedSurf = pygame.transform.rotate(surf, degree)

rotRect = rotatedSurf.get_rect()
rotRect.center = oldCenter

screen.blit(rotatedSurf, rotRect)
degree += 5
if degree > 360:
    degree = 0
'''


'''
F_Left_Wheel = pygame.surface.Surface((5,5))
F_Left_Wheel.fill(pygame.Color("white"))
pygame.draw.rect(F_Left_Wheel, pygame.Color("white"),frame,0)
F_Left_Wheel.set_colorkey(pygame.Color("white"),pygame.RLEACCEL)
F_Left_Wheel = F_Left_Wheel.convert()
        #Middle Left Wheel
M_Left_Wheel = pygame.surface.Surface((10, 10))
M_Left_Wheel.fill(pygame.Color("white"))
pygame.draw.rect(M_Left_Wheel, pygame.Color("white"),25,0)
M_Left_Wheel.set_colorkey(pygame.Color("white"),pygame.RLEACCEL)
M_Left_Wheel = M_Left_Wheel.convert()
        #Back Left Wheel
B_Left_Wheel = pygame.surface.Surface((10, 10))
B_Left_Wheel.fill(pygame.Color("white"))
pygame.draw.rect(B_Left_Wheel, pygame.Color("white"),25,0)
B_Left_Wheel.set_colorkey(pygame.Color("white"),pygame.RLEACCEL)
B_Left_Wheel = B_Left_Wheel.convert()
        #Front Right Wheel
F_Right_Wheel = pygame.surface.Surface((10, 10))
F_Right_Wheel.fill(pygame.Color("white"))
pygame.draw.rect(F_Right_Wheel, pygame.Color("white"),25,0)
F_Right_Wheel.set_colorkey(pygame.Color("white"),pygame.RLEACCEL)
F_Right_Wheel = F_Right_Wheel.convert()
        #Middle Right Wheel
M_Right_Wheel = pygame.surface.Surface((10, 10))
M_Right_Wheel.fill(pygame.Color("white"))
pygame.draw.rect(M_Right_Wheel, pygame.Color("white"),25,0)
M_Right_Wheel.set_colorkey(pygame.Color("white"),pygame.RLEACCEL)
M_Right_Wheel = M_Right_Wheel.convert()
        #Back Right Wheel
B_Right_Wheel = pygame.surface.Surface((10, 10))
B_Right_Wheel.fill(pygame.Color("white"))
pygame.draw.rect(B_Right_Wheel, pygame.Color("white"),25,0)
B_Right_Wheel.set_colorkey(pygame.Color("white"),pygame.RLEACCEL)
B_Right_Wheel = B_Right_Wheel.convert()
'''
degree = 0
while True:
    #Check events
    pygame.event.pump()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Background
    screen.fill(pygame.Color("black"))

    #Get joysticks axes
    Lx = Leftjoy.get_axis(0)
    Ly = Leftjoy.get_axis(1)

    Rx = Rightjoy.get_axis(0)
    Ry = Rightjoy.get_axis(1)

    #Move to coords
    # x*amplitude+(centre offset (window size/2))-(crosshair offset (xh size/2))
    screen.blit(Leftcrosshair, ((Lx*100)+140, (Ly*100)+140))
    screen.blit(Rightcrosshair, ((Rx*100)+140, (Ry*100)+140))
    
    #screen.blit(F_Left_Wheel, 300, 300)
    

    #Draw joystick limit box
    pygame.draw.rect(screen, pygame.Color("red"), frame, 1)
    #ten = pygame.draw.rect(screen, pygame.Color("white"), frame,0)

    #screen.blit(F_Left_Wheel,(300,300))
    #screen.blit(ten,((Lx*100)+140, (Ly*100)+140))
    surf = pygame.Surface((20,20))
    surf.fill(pygame.Color("black"))
    surf.set_colorkey(pygame.Color("black"))
    big = pygame.Rect(0,0,20,30)
    pygame.draw.rect(surf, (255,255,255 ), big)

    point = 200, 10

    blittedRect = screen.blit(surf, point)
    oldCenter = blittedRect.center
    rotatedSurf = pygame.transform.rotate(surf, degree)

    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter

    screen.blit(rotatedSurf, rotRect)
    degree += 5
    if degree > 360:
        degree = 0
    
    #Write the display
    pygame.display.flip()
    clk.tick(40)
    











    
                                
