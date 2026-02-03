import pytest
import src.busTickets as module

"""
if under 3, 0
if under 19 and over 3 and student, 2
if over 65, 0
if over 19 and under 65, 4
"""

# def test_under_3_returns_0():
#     assert module.calculate_ticket_price(2) == 0

# def test_over_65_returns_0():
#     assert module.calculate_ticket_price(65) == 0

# def test_under_19_student_returns_2():
#     assert module.calculate_ticket_price(18, True) == 2

# def test_under_19_nonstudent_returns_4():
#     assert module.calculate_ticket_price(18, False) == 4

# def test_over_19_returns_4():
#     assert module.calculate_ticket_price(30) == 4


"""
    speed - limit > 10 => ticket and summons
    speed - limit >0 & <=10 => ticket only
    speed - limit <= 0 => no ticket or summons
"""

def test_not_speeding():
    assert module.get_speeding_penalties(20, 30) == (False, False)

def test_speeding_less_than_10():
    assert module.get_speeding_penalties(25, 20) == (True, False)

def test_speeding_more_than_10():
    assert module.get_speeding_penalties(31, 20) == (True, True)


"""
    up to 10 miles and value over 100 => 0
    up to 10 miles and value under 100 => 5
    over 10 miles => 10
    over 20 miles => 15
    over 30 miles => 15 + 50 * (m-30) 
"""

def test_under_10_miles_over_100_gbp():
    assert module.get_delivery_price(10, 100) == 0

def test_under_10_miles_under_100_gbp():
    assert module.get_delivery_price(10, 99) == 5

def test_between_10_and_20_miles():
    assert module.get_delivery_price(20, 100) == 10

def test_between_20_and_30_miles():
    assert module.get_delivery_price(30, 100) == 15

def test_over_30_miles():
    assert module.get_delivery_price(35, 100) == 17.5