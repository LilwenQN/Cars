def calculate_ticket_price(age: int, is_student:bool = False) -> int:
    if age < 3 or age >= 65:
        return 0
    elif age < 19 and is_student:
        return 2
    return 4

def get_speeding_penalties(currentSpeed: int, limit: int) -> tuple[bool, bool]:
    if currentSpeed < limit:
        return (False, False)
    elif currentSpeed - limit <= 10:
        return (True, False)
    else:
        return (True, True)

def get_delivery_price(distance: float, price: float) -> float:
    if distance <= 10:
        if price >= 100:
            return 0
        else:
            return 5
    elif distance > 20:
        addition = 0
        if distance > 30:
            addition = distance - 30
            addition *= 0.5
        return 15 + addition
    elif distance > 10:
        return 10
    
    