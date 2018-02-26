class Value:
    def __init__(self, value, cordinateX, cordinateY):
        self.value = value
        self.X = cordinateX
        self.Y = cordinateY
    
    def print(self):
        print()
        print('{0:^25}'.format('Get Element'))
        print('+-------+-------+-------+')
        print('| X cor | Y cor | Value |')        
        print('+-------+-------+-------+')
        print('| {0:>5} | {1:>5} | {2:>5} |'.format(self.X, self.Y, self.value))        
        print('+-------+-------+-------+')   

class Matrix:
    def __init__(self, mtr=None):
        if mtr == None:
            self.mtr = []
        else:
            for item in mtr:
                if item.value != 0:
                    self.mtr.append(item)

    def getElement(self, X, Y):
        for item in self.mtr:
            if item.X == X and item.Y == Y:
                return item
        else:
            return Value(0,0,0)

    def appendElement(self, value):
        for item in self.mtr:
            if item.X == value.X and item.Y == value.Y:
                return False
        self.mtr.append(value)
        return True
    
    def print(self):
        print('{0:^25}'.format('Print Matrix'))
        print('+-------+-------+-------+')
        print('| X cor | Y cor | Value |')        
        print('+-------+-------+-------+')        
        for item in self.mtr:
            print('| {0:>5} | {1:>5} | {2:>5} |'.format(item.X, item.Y, item.value))
        print('+-------+-------+-------+')     

def main():
    matrix = Matrix()
    
    matrix.appendElement(Value(3, -102, 12))
    matrix.appendElement(Value(4, -103, 14))
    matrix.appendElement(Value(3, -10, 122))
    matrix.appendElement(Value(12, 33, 12))
    matrix.appendElement(Value(14, 53, 52))

    matrix.print()

    elem = matrix.getElement(-102, 12)
    elem.print()

    elem = matrix.getElement(-102, 0)
    elem.print()

if __name__ == '__main__':
    main()
