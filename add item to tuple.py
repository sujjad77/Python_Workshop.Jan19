_tuple = (1, 2, 3, 4, 5, 6)
#1
_tuple = _tuple + (1, 7, 8 ,9)
print(_tuple)
#2 in specific position
_tuple =_tuple[:2] + (1, 7, 8, 9) + _tuple[:2]
print(_tuple)