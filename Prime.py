from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub() 
color_sensor_E = ColorSensor('E')
color_sensor_F = ColorSensor('F')

motor_A =  Motor('A') # Set the motor port to the motor.
motor_B = Motor('B') # Set the motor port to the motor.

motor_A.set_default_speed(-30) # Set the default speed of the motor.
motor_B.set_default_speed(30) # Set the default speed of the motor.

motor_A.set_stop_action('brake') # Activate the brakes when the motor stops. The other conditions are 'hold' and 'coast'.
motor_B.set_stop_action('brake') # Activate the brakes when the motor stops.

motor_A_flag = 0 # Create a flag for motor A and set it to OFF.
motor_B_flag = 0 # Create a flag for motor B and set it to OFF.

def stop_at(color):
    motor_A_flag = 0 # Reset the flag for motor A to OFF.
    motor_B_flag = 0 # Reset the flag for motor B to OFF.

    # Move forward.
    motor_A.start()
    motor_B.start()

    while (motor_A_flag == 0) or (motor_B_flag == 0): # Repeat while both sensors ever detect black color.
        if color_sensor_E.get_color() == color: # If the color sensor on port E detect the desired color
            motor_A.stop() # stop the motor an port A and
            motor_A_flag = 1 # set the flag for motor A to ON.
        if color_sensor_F.get_color() == colour: # If the color sensor on port F detect the desired color
            motor_B.stop() # stop the motor an port B and
            motor_B_flag = 1 # set the flag for motor B to ON.

stop_at('black')
stop_at('white')
raise SystemExit # Close the program.