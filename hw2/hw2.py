from cleaner import *
from math import *

cleaner = Cleaner()

# PROBLEM 1

p1 = """
4.10  	  3.44  	  3.41  	  3.35  	  3.50  	  2.57  	  2.39  	  4.34  	  2.60  
4.34  	  2.30  	  3.77  	  2.66  	  3.98  	  3.32  	  3.29  	  3.62
"""

data = cleaner.clean(p1)

size = len(data)
x_i = sum(data)/size
x_i2 = sum([i ** 2 for i in data])/size

print(x_i)
print(x_i2)

variance = (x_i2 - (x_i**2)/size)/(size - 1)
print(variance)		# Variance  
print(sqrt(variance)) # Std dev

# PROBLEM 2
urban = """7.0	  6.0	  10.0	  33.0	  1.0	  4.0	  81.0	  19.0	  37.0	  16.0	  23.0"""
farm = """3.0	  16.0	  13.0	7.0	8.0	7.0	2.0	19.0	7.0	9.7	24.0	  9.3	  1.0	  1.0	  0.4"""

data = cleaner.clean(urban)
xbar = sum(data)/ len(data)
print("\nUrban average: {}".format(xbar))
print("Urban median: {}".format(median(data)))
print("Urban trimmed average: {}".format(mean(data[1:-1])))
print("Urban samples: {}".format(len(data)))

data = cleaner.clean(farm)
xbar = sum(data)/ len(data)
print("\nFarm average: {}".format(xbar))
print("Farm median: {}".format(median(data)))
print("Farm trimmed average: {}".format(mean(data[1:-1])))
print("Farm samples: {}".format(len(data)))
