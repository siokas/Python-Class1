from Ev3Brick import Ev3Brick
from Motor import Motor
from Port import Port
from DriveBase import DriveBase
    
ev3 = Ev3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

first_position = 100

robot.straight(1000)

robot.straight(-600)

robot.straight(250)

robot.straight(-100)

print(robot.position)