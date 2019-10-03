data = """
0.173	0.163	0.173	0.135	0.199	0.079	0.048	0.030
"""

data = data.replace("\n", "").split("\t")
data = [float(i) for i in data]
print(data)

