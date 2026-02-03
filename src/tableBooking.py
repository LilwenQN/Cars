class Resturant:
    tables: dict = None

    def __init__(self):
        self.tables = {}
    
    def __init__(self, _tables: dict):
        self.tables = _tables
    
    def addTable(self, _tableNumber: int, _seats: int, _isOutside: bool):
        if self.tables[_tableNumber] == None:
            newTable: Table = Table(_tableNumber, _seats, _isOutside)
            self.tables[_tableNumber] = newTable

class Table:
    tableNumber: int = None
    booking: str = None
    seats: int = None
    isOutside: bool = None

    def __init__(self, _tableNumber: int, _seats: int, _isOutside: bool):
        self.tableNumber = _tableNumber
        self.seats = _seats
        self.isOutside = _isOutside