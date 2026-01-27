class Cars:
    CurrentSpeed = 0
    MaxSpeed = 0
    FuelLevel = 0
    FuelCapacity = 100

    def __init__(self):
        pass

    def Accelerate(self, amount: int):
        if (amount > self.MaxSpeed-self.CurrentSpeed):
            amount = self.MaxSpeed-self.CurrentSpeed
        if (self.FuelLevel - amount <= 0):
            amount = self.FuelLevel
        self.CurrentSpeed += amount
        self.FuelLevel -= amount

    def Brake(self, amount: int):
        if (amount > self.CurrentSpeed):
            amount = self.CurrentSpeed

        self.CurrentSpeed -= amount

    def Refuel(self, amount: int):
        self.FuelLevel += amount
        if (self.FuelLevel > self.FuelCapacity):
            self.FuelLevel = self.FuelCapacity