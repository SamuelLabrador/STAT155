from cleaner import *

cleaner = Cleaner()
displayer = Displayer()

# PROBLEM 1

p1 = """
5.9	7.2	7.3	6.3	8.1	6.8	7.0	7.6	6.8	6.5	7.0	6.3	7.9	 9.0
8.2	8.7	7.8	9.7	7.4	7.7	9.7	7.8	7.7	11.6	11.3	11.8	10.7
"""

data = cleaner.clean(p1)
size = len(data)

print(data)
print('Representative stength value: ', median(data))

threshold = 0
for value in data:
    if value > 10:
        threshold += 1

print('Proportion: ', threshold / size)

# PROBLEM 2
p2 = """
 1  	  1  	  3  	  12  	  11  	  15  	  19  	  10  	  12  	  4  	5  	3  	1  	2  	1  
"""
data = cleaner.clean(p2, sort=False)
size = sum(data)

print('\nFrequency Count: ', size)
print('At least 5 particles:', sum(data[5:]))
print('At least 5 to 10, inclusive:', sum(data[5:11]))
print('At least 5 to 10, exclusive:', sum(data[6:10]))


# PROBLEM 3
p3 = """
.31	.35	.36	.36	.37	.38	.40	.40	.40
.41	.41	.42	.42	.42	.42	.42	.43	.44
.45	.46	.46	.47	.48	.48	.48	.51	.54
.54	.55	.58	.62	.66	.66	.67	.68	.75
""".replace(".", "")

data = cleaner.clean(p3)
print('-->')
displayer.stemLeaf(data, 10)

p4 = """
0	19.3	37.8	62.8	77.7	87.6	94.6	96.1	98.7	99.0	99.5	99.6	99.8	100.0
"""

print('')
data = cleaner.clean(p4)
data = [ (data[value] - data[value - 1]) for value in range(1, len(data))]
[print(value) for value in data]
print('sum of 1350+: ', sum(data[-5:]))
print('Loads between 750 and 1350: ', sum(data[6: 9]))


p5 = """
1280	5320	4390	2100	1240	3060	4770
1050	360	3330	3380	340	1000	960
1320	530	3350	540	3870	1250	2400
960	1120	2120	450	2250	2320	2400
3150	5700	5220	500	1850	2460	5850
2700	2730	1670	100	5770	3150	1890
510	240	396	1419	2109
"""

data = cleaner.clean(p5)
size = len(data)
print('\nData set size: ', size)
displayer.stemLeaf(data, 1000)
print('Proportion of subdivisions < 2000: ', 23/size)


# PROBLEM 6
p6 = """
0.173	0.163	0.173	0.135	0.199	0.079	0.048	0.030
"""

data = cleaner.clean(p6, sort=False)
print('\n', data)
print('Angles less than 15 degrees: ', sum(data[0:3]))
print('Angles at least 15 degrees: ', sum(data[3:]))

# PROBLEM 7

p7 = """
4   1   2   4   0   1   3   2   0   5   3   3   1   3   2   4   7   0   2   3
2   4   2   1   3   1   1   3   4   1   2   3   2   2   8   4   5   1   3   1
7   0   2   3   2   1   0   6   4   2   1   6   0   3   3   3   6   1   2   3
"""

data = cleaner.clean(p7)
displayer.histogram(data)

p8_y = """1	0	1	0	0	2	0	1	1	1	2	1	0	0	1	1	0	1	1	1	1	0	0	0	1	1	2	0	1	2	2	1	1	0	2	1	1	0	1	5	0	3	0	1	1	0	0"""
p8_z = """1	8	6	1	1	5	3	0	0	4	4	0	0	1	2	1	4	0	4	0	3	0	1	1	0	1	3	2	4	6	6	0	1	1	8	3	3	5	0	5	2	3	1	0	0	0	3
"""
data = cleaner.clean(p8_y)
displayer.histogram(data)

data = cleaner.clean(p8_z)
displayer.histogram(data)

p9 = """
82
109
119
96
110
121
99
110
122
102
111
122
103
113
127
103
113
132
106
113
136
107
113
140
108
115
146
108
115
108
118
108
118
"""

print('\n\n')
data = cleaner.clean(p9)
displayer.stemLeaf(data, 10)

p10 = """772	  204	  127	    50	    33	    28	    19	    19	      6	      7	      6	      7	      4	      4	      5	     3	  3"""
data = cleaner.clean(p10)

print('\n\n')
print(sum(data))