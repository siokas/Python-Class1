class DriveBase:

    # Define Variables
    motor1 = 0
    motor2 = 0
    wheel_diameter = 0
    axle_track = 0
    position = 0
    position_y = 0
    sensors = []

    #Define INIT function
    def __init__(self,
                 left_motor,
                 right_motor,
                 wheel_diameter,
                 axle_track,
                 sensors=[]):
        self.motor1 = left_motor
        self.motor2 = right_motor
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track
        self.sensors = sensors

        print("Your drive base is ready")

    def straight(self, mm):
        self.position = self.position + mm
        print(mm)

    def turn(self, degrees):
        self.position_y = self.position_y + degrees
        print("robot has just turned", degrees, "degrees!")

    def circle(self):
        self.turn(360)

    def get_degrees(self):
        return self.position_y - ((self.position_y / 360) * 360)

    def print_sensor(self):
        for sensor in self.sensors:
            print(sensor.type)
