from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub() 



motor_pair = MotorPair('A', 'B') # Set the motor ports in the motor_pair.

motor_pair.set_default_speed(30) # Set the default speed of the motor_pair.

 # Set the distance that the robot travels for one rotation its wheels. The value comes from# the diameter of the wheel  multiplied by "π" (3.14).
motor_pair.set_motor_rotation(22, 'cm')

# Activate the brakes when the robot stops. The other conditions are 'hold' and 'coast'.
motor_pair.set_stop_action('brake')


wait_for_seconds(1) # Wait for one second.

#Reset the Gyro sensor. The current yaw angle value is equal to 0.
hub.motion_sensor.reset_yaw_angle() 

motor_pair.start(steering = 100) # Turn left around the center of the wheelbase. Leftward because of steering=-100 parameter.

# To program the robot to wait until the robot has turned, we need to define a fuction that checks if the robot has turned.
def left_turn_end(): # Define the function
    return hub.motion_sensor.get_yaw_angle() > 90 # Return true or false depending on the yaw angle value.

wait_until(left_turn_end) # Wait until the left turn end. left_turn_end is a function that defines the left turn

motor_pair.stop() # Stop moving. Hit the brakes! Remember the motor_pair.set_stop_action('brake') statement/setting?

raise SystemExit # Close the program.