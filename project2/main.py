from Ev3Brick import Ev3Brick
from Motor import Motor
from Sensor import Sensor
from Port import Port
from DriveBase import DriveBase

ev3 = Ev3Brick()

left_motor = Motor(port=Port.B, isBig=True)
right_motor = Motor(Port.C)

touch_sensor = Sensor(port=Port.S1, type="touch")
color_sensor = Sensor(port=Port.S2, type="color")

robot = DriveBase(left_motor,
                  right_motor,
                  55.5,
                  104,
                  sensors=[touch_sensor, color_sensor])
robot.print_sensor()

first_position = 0

# robot.straight(1000)

robot.turn(50)

robot.turn(50)
robot.turn(450)

robot.turn(6650)
robot.turn(150)
robot.turn(50)

robot.turn(450)

print(robot.get_degrees())

# print(robot.position)