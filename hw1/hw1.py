from cleaner import *

cleaner = Cleaner()

p7 = """
4   1   2   4   0   1   3   2   0   5   3   3   1   3   2   4   7   0   2   3
2   4   2   1   3   1   1   3   4   1   2   3   2   2   8   4   5   1   3   1
7   0   2   3   2   1   0   6   4   2   1   6   0   3   3   3   6   1   2   3
"""

data = cleaner.clean(p7)


p8_y = """1	0	1	0	0	2	0	1	1	1	2	1	0	0	1	1	0	1	1	1	1	0	0	0	1	1	2	0	1	2	2	1	1	0	2	1	1	0	1	5	0	3	0	1	1	0	0"""
p8_z = """1	8	6	1	1	5	3	0	0	4	4	0	0	1	2	1	4	0	4	0	3	0	1	1	0	1	3	2	4	6	6	0	1	1	8	3	3	5	0	5	2	3	1	0	0	0	3
"""
data = cleaner.histogram(p8_y)
data = cleaner.histogram(p8_z)

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
data = cleaner.stemLeaf(10, p9)

p10 = """772	  204	  127	    50	    33	    28	    19	    19	      6	      7	      6	      7	      4	      4	      5	     3	  3"""
data = cleaner.clean(p10)

print('\n\n')
print(sum(data))