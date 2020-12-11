class DriveBase:

    # Define Variables
    motor1 = 0
    motor2 = 0
    wheel_diameter = 0
    axle_track = 0
    position = 0

    #Define INIT function
    def __init__(self, left_motor, right_motor, wheel_diameter, axle_track):
        self.motor1 = left_motor
        self.motor2 = right_motor
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track

        print("Your drive base is ready")

    def straight(self, mm):
        self.position = self.position + mm
        print(mm)