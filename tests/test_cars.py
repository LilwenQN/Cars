import pytest
from src.cars import Cars

def test_car_creation():
    car = Cars()
    assert car.CurrentSpeed == 0
    assert car.MaxSpeed == 0
    assert car.FuelLevel == 0

def test_accelerate_allvalid():
    car = Cars()
    car.MaxSpeed = 100
    car.FuelLevel = 50
    car.Accelerate(30)
    assert car.CurrentSpeed == 30
    assert car.FuelLevel == 20

def test_accelerate_exceed_maxspeed():
    car = Cars()
    car.MaxSpeed = 100
    car.FuelLevel = 50
    car.CurrentSpeed = 90
    car.Accelerate(20)
    assert car.CurrentSpeed == 100
    assert car.FuelLevel == 40

def test_accelerate_insufficient_fuel():
    car = Cars()
    car.MaxSpeed = 100
    car.FuelLevel = 10
    car.Accelerate(30)
    assert car.CurrentSpeed == 10
    assert car.FuelLevel == 0

def test_accelerate_no_fuel():
    car = Cars()
    car.MaxSpeed = 100
    car.FuelLevel = 0
    car.Accelerate(30)
    assert car.CurrentSpeed == 0
    assert car.FuelLevel == 0

def test_brake_allvalid():
    car = Cars()
    car.CurrentSpeed = 50
    car.Brake(20)
    assert car.CurrentSpeed == 30

def test_brake_exceed_currentspeed():
    car = Cars()
    car.CurrentSpeed = 30
    car.Brake(50)
    assert car.CurrentSpeed == 0

def test_brake_speedzero():
    car = Cars()
    car.CurrentSpeed = 0
    car.Brake(20)
    assert car.CurrentSpeed == 0

def test_refuel_allvalid():
    car = Cars()
    car.FuelLevel = 50
    car.Refuel(30)
    assert car.FuelLevel == 80

def test_refuel_exceed_capacity():
    car = Cars()
    car.FuelLevel = 90
    car.Refuel(20)
    assert car.FuelLevel == 100