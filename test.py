import datetime
from datetime import time

a = time(10, 30)
b = time(10, 40)
print(a)
print(b)
new_a = datetime.datetime.combine(datetime.date(1, 1, 1), a)
new_b = datetime.datetime.combine(datetime.date(1, 1, 1), b)
print(new_a)
print(new_b)
c = new_b - new_a
print('Difference: ', c)
print(type(c))

