class Motor:

    isBig = False

    def __init__(self, port, isBig=False):
        self.isBig = isBig
        if isBig:
            print(port + " MOTOR is big")
        else:
            print(port + " MOTOR is small")
