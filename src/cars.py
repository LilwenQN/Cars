class Cars:
    CurrentSpeed = 0
    MaxSpeed = 0
    FuelLevel = 0

    def Cars():
        pass

    def Accelerate(self):
        self.CurrentSpeed += 1
        self.FuelLevel -= 1

    def Brake(self):
        self.CurrentSpeed -= 1
    
    def Refuel(self):
        self.FuelLevel += 1
