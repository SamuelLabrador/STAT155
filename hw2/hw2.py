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

var = (x_i2 - (x_i**2)/size)/(size - 1)
print(var)		# Variance  
print(sqrt(var)) # Std dev

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


# PROBLEM 3
p3 = """
2776  	  2903  	  3000  	  2826  	  2879
"""

data = cleaner.clean(p3)

var = variance(data)
print("\nSpecimens mean: ", mean(data))
print("Specimens median: ", median(data))
print("Specimens sample variance: {}".format(var))


# PROBLEM 4
p4 = """
14.5  	  12.6  	  17.6  	  14.5  	  12.3  	  10.7  	  9.5  	  8.2
"""

data = cleaner.clean(p4)

print("\nInjection pressure average: ", mean(data))
print("Injection pressure median: ", median(data))
print("Injection pressure trimmed mean @ 12.5%: ", trimmed_mean(data, 0.125))

# 12.3 is one of the median values
print("Smallest increase of smalest sample: ", 12.3 - 8.2) 

# PROBLEM 5

p5 = """
    115.9  	  116.4  	  115.1  	  116.4  	  114.8
"""

data = cleaner.clean(p5)
average = mean(data)

print("Mean of data: ", average)
for value in data:
    print('{} deviation: {}'.format(value, (value - average) ** 2))

print('Variance: ', variance(data))
print('Standard Deviation: ', std_deviation(data))

data = [value - 100 for value in data]
print('Variance of transformed data (value - 100): ', variance(data))


# PROBLEM 6
p6 = """
33.1 	 47.1 	 30.6 	 29.7 	 29.0 	 28.9 	 29.8 	 28.0 	 23.1 	 27.9
"""

data = cleaner.clean(p6)

print('\nRange: ', stat_range(data))
print('Variance: ', variance(data))
print('Std Deviation: ', std_deviation(data))

p7 = """
242	191	157	188	178	174	180
203	212	183	206	175	191	204
"""

data = cleaner.clean(p7)
print('\nAverage: ', mean(data))
print('Median: ', median(data))

i = data.index(242)
data[i] = 256
data.sort()

print('242 --> 256 Average: ', mean(data))
print('242 --> 256 Median: ', median(data))
print('Trimmed mean: ', mean(data[1:-1]))
print('Trim percentage: ', (len(data) - 2) / len(data))

print('Data set size: ', len(data))

average = 119.7692
outlier = 165
size = 14
average = average + (outlier - average) / size

print('Entire sample average: ', average)

# PROBLEM 8
p8 = """
F   F   S   S   S   F   F   S   S   F
"""

fail = p8.count("F")
succ = p8.count("S")
size = fail + succ

average = succ / size

print('\nFails: ', fail)
print('Passes: ', succ)
print('Average: ', average)
print('Required S\'s: ', int(25 * 0.8))

# PROBLEM 9
p9 = """
0.737	0.843	0.878	0.904	0.925	0.937	0.988	0.993
1.030	1.050	1.082	1.120	1.146	1.174	1.236	1.396
"""

data = cleaner.clean(p9)
average = mean(data)
med = median(data)
size = len(data)

print('\nAverage: ', average)
print('Median: ', med)
print(data)
print('Maximum change: ', data[-1] - data[8])


p10 = """
385	351	354	360	378	424	321	397	404
374	376	371	364	367	364	328	337	395
391	368	377	356	352	408	331	397
"""

data = cleaner.stemLeaf(10, p10)
average = mean(data)
med = median(data)

print('\n', data)
print('Average: ', average)
print('Median: ', med)
print('Data set size: ', len(data))
print('Smallest Change: ', data[-1] - data[13])

data = [ value / 60 for value in data]

average = mean(data)
med = median(data)
print('Average: ', average)
print('Median: ', med)