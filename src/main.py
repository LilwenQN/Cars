from cars import Cars

car1 = Cars()
car2 = Cars()

car1.FuelLevel = 100
car1.CurrentSpeed = 30
car1.MaxSpeed = 80
car2.FuelLevel = 50
car2.CurrentSpeed = 60
car2.MaxSpeed = 80

print(car1.CurrentSpeed, car1.MaxSpeed, car1.FuelLevel)
print(car2.CurrentSpeed, car2.MaxSpeed, car2.FuelLevel)

car1.Accelerate(1)
print(car1.CurrentSpeed, car1.MaxSpeed, car1.FuelLevel)
car1.Brake(1)
print(car1.CurrentSpeed, car1.MaxSpeed, car1.FuelLevel)
car1.Refuel(1)
print(car1.CurrentSpeed, car1.MaxSpeed, car1.FuelLevel)