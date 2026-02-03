import pytest
from src.tableBooking import *

"""
    ADD TABLE
        tableNumber exists
        assignedBooking = None
        numberOfSeats = assigned number
        isOutside = assigned
        resturant.tables gets new table

        fails if resturant.tables contains tableNumber
"""

@pytest.fixture
def resturant():
    newRest = Resturant()
    return newRest

def test_create_table_valid_number(resturant):
    resturant.addTable(1, 4, False)
    assert resturant.getTableBooking(1) == None
    assert resturant.getTableSeats(1) == 4
    assert resturant.isOutside(1) == False