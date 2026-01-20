class Cars:
    CurrentSpeed = 0
    MaxSpeed = 0
    FuelLevel = 0

    def __init__(self):
        pass

    def Accelerate(self, amount):
        if (amount > self.MaxSpeed-self.CurrentSpeed):
            amount = self.MaxSpeed-self.CurrentSpeed
        self.CurrentSpeed += amount
        self.FuelLevel -= amount

        if (self.FuelLevel <= 0):
            self.CurrentSpeed = 0

    def Brake(self, amount):
        if (amount > self.CurrentSpeed):
            amount = self.CurrentSpeed

        self.CurrentSpeed -= amount
    
    def Refuel(self, amount):
        self.FuelLevel += amount
        if (self.FuelLevel > 100):
            self.FuelLevel = 100
