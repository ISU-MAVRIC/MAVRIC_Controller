#!/usr/bin/env python


print "\n====================================="
print "         MAVRIC CONTROLLER"
print "====================================="

import pygame.joystick
import servo
import DisplayOfAxis

pygame.init()
pygame.joystick.init()
 

done = False
joy = []

joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    # No joysticks!
    print ("Error, I didn't find any joysticks.")
else:
    print "\n%d joystick(s) detected." % pygame.joystick.get_count()
    Ljoystick = pygame.joystick.Joystick(0)
    Rjoystick = pygame.joystick.Joystick(1)
    Ljoystick.init()
    Rjoystick.init()
    joy.append(Ljoystick)
    joy.append(Rjoystick)

    
while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
             
    # As long as there is a joystick
    if joystick_count != 0:
     
        #Left joystick axes
        Lx_axis_pos = Ljoystick.get_axis(0) #X axis
        Ly_axis_pos = Ljoystick.get_axis(1) #Y axis
        Lt_axis_pos = Ljoystick.get_axis(2) #Throttle axis
        Lz_axis_pos = Ljoystick.get_axis(3) #Z axis

        #Right joystick axes
        Rx_axis_pos = Rjoystick.get_axis(0) #X axis
        Ry_axis_pos = Rjoystick.get_axis(1) #Y axis
        Rt_axis_pos = Rjoystick.get_axis(2) #Throttle axis
        Rz_axis_pos = Rjoystick.get_axis(3) #Z axis       
         
        #Coordinates
        L_x_coord=int(round(Lx_axis_pos * 90, 0) + 90) 
        L_y_coord=int(round(Ly_axis_pos * 90, 0) + 90)
        L_t_coord=int(round(Lt_axis_pos * 90, 0) + 90)
        L_z_coord=int(round(Lz_axis_pos * 90, 0) + 90)

        R_x_coord=int(round(Rx_axis_pos * 90, 0) + 90)
        R_y_coord=int(round(Ry_axis_pos * 127, 0) + 127) #Motor speeds from 0-127-255
        R_t_coord=int(round(Rt_axis_pos * 90, 0) + 90)
        R_z_coord=int(round(Rz_axis_pos * 90, 0) + 90)

        #Progress Bar Coordinates
        L_x_bar=int(round(Lx_axis_pos * 50, 0) + 50) 
        L_y_bar=int(round(Ly_axis_pos * 50, 0) + 50)
        L_t_bar=int(round(Lt_axis_pos * 50, 0) + 50)
        L_z_bar=int(round(Lz_axis_pos * 50, 0) + 50)

        R_x_bar=int(round(Rx_axis_pos * 50, 0) + 50)
        R_y_bar=int(round(Ry_axis_pos * 50, 0) + 50)
        R_t_bar=int(round(Rt_axis_pos * 50, 0) + 50)
        R_z_bar=int(round(Rz_axis_pos * 50, 0) + 50)

        #Coordinates of Left Joystick progress bars
        DisplayOfAxis.move(0, L_x_bar)
        DisplayOfAxis.move(1, L_y_bar)
        DisplayOfAxis.move(3, L_z_bar)
        DisplayOfAxis.move(2, L_t_bar)
        
        #Coordinates of Right Joystick progress bars
        DisplayOfAxis.move(4, R_x_bar)
        DisplayOfAxis.move(5, R_y_bar)
        DisplayOfAxis.move(7, R_z_bar)
        DisplayOfAxis.move(6, R_t_bar)
        
#Servo Movements servo.move("servo", "angle")
        #Left joystick buttons
        
        L_T_btn_pos = Ljoystick.get_button(0) #Left trigger
        if L_T_btn_pos == 1:
            servo.move(99,180)
            print "Left Trigger Pressed"
        else:
            servo.move(0,0)
        L_2_btn_pos = Ljoystick.get_button(1) #Left button 2
        if L_2_btn_pos == 1:
            servo.move(0,180)
            print "Left Button 2 Pressed"
        else:
            servo.move(0,0)
        L_3_btn_pos = Ljoystick.get_button(2) #Left button 3
        if L_3_btn_pos == 1:
            servo.move(0,90)
            print "Left Button 3 Pressed"
        else:
            servo.move(0,0)
        L_4_btn_pos = Ljoystick.get_button(3) #Left button 4
        if L_4_btn_pos == 1:
            servo.move(0,180)
            print "Left Button 4 Pressed"
        else:
            servo.move(0,0)
        L_5_btn_pos = Ljoystick.get_button(4) #Left button 5
        if L_5_btn_pos == 1:
            servo.move(0,180)
            print "Left Button 5 Pressed"
            quit()
        else:
            servo.move(0,0)
        L_6_btn_pos = Ljoystick.get_button(5) #Left button 6
        if L_6_btn_pos == 1:
            servo.move(0,180)
            print "Left Button 6 Pressed"
        else:
            servo.move(0,0)
        L_7_btn_pos = Ljoystick.get_button(6) #Left toggle button
        if L_7_btn_pos == 1:
            servo.move(0,180)
            print "Left Toggle Button Pressed"
        else:
            servo.move(0,0)

        #Right joystick buttons
        R_T_btn_pos = Rjoystick.get_button(0) #Right trigger
        if R_T_btn_pos == 1:
            servo.move(99,180)
            print "Right Trigger Pressed"
        else:
            servo.move(99,0)
        R_2_btn_pos = Rjoystick.get_button(1) #Right button 2
        if R_2_btn_pos == 1:
            servo.move(0,180)
            print "Right Button 2 Pressed"
        else:
            servo.move(0,0)
        R_3_btn_pos = Rjoystick.get_button(2) #Right button 3
        if R_3_btn_pos == 1:
            servo.move(0,180)
            print "Right Button 3 Pressed"
        else:
            servo.move(0,0)
        R_4_btn_pos = Rjoystick.get_button(3) #Right button 4
        if R_4_btn_pos == 1:
            servo.move(0,180)
            print "Right Button 4 Pressed"
        else:
            servo.move(0,0)
        R_5_btn_pos = Rjoystick.get_button(4) #Right button 5
        if R_5_btn_pos == 1:
            servo.move(0,180)
            print "Right Button 5 Pressed"
        else:
            servo.move(0,0)
        R_6_btn_pos = Rjoystick.get_button(5) #Right button 6
        if R_6_btn_pos == 1:
            servo.move(0,180)
            print "Right Button 6 Pressed"
        else:
            servo.move(0,0)
        R_7_btn_pos = Rjoystick.get_button(6) #Right toggle button
        if R_7_btn_pos == 1:
            servo.move(0,180)
            print "Right Toggle Button Pressed"       
        else:
            servo.move(0,0)

        #Left Joystick Hat
        L_h_hat_pos = Ljoystick.get_hat(0)[0] #Left hat x direction
        if L_h_hat_pos == -1:
            servo.move(1,90)
        elif L_h_hat_pos == 1:
            servo.move(1, 180)
        elif L_h_hat_pos == 0:
            servo.move(0,0)
        L_v_hat_pos = Ljoystick.get_hat(0)[1] #Left hat y direction
        if L_v_hat_pos == -1:
            servo.move(4,90)
        elif L_v_hat_pos == 1:
            servo.move(4, 180)
        elif L_v_hat_pos == 0:
            servo.move(4,0)
        
        #Right Joystick Hat
        R_h_hat_pos = Rjoystick.get_hat(0)[0] #Right hat x direction
        R_v_hat_pos = Rjoystick.get_hat(0)[1] #Right hat y direction
        
#from DisplayOfAxis import Progress
#progress = Progress()

    #Axes Moves
    servo.move(2, L_x_coord)
    servo.move(3, L_y_coord)
    servo.move(0, L_y_coord)
    servo.move(0, L_y_coord)
    servo.move(6, L_z_coord)
    servo.move(0, L_t_coord)

    servo.move(0, R_x_coord)
    servo.move(0, R_y_coord)#Speed of Right wheels
    servo.move(0, R_y_coord)
    servo.move(0, R_y_coord)
    servo.move(0, R_z_coord)
    servo.move(0, R_t_coord)
 
pygame.quit()
