class Cleaner():

	# Formats data to space sparated values
	# data should be a string of the raw data
	# dataType should be int, or float
	def __init__(self):
		pass		

	def clean(self, data=""):
		data = data.replace("\n", " ")	# Get rid of newlines
		data = data.replace("\t", " ")	# Get rid of tabs

		# Get rid of extra spaces
		while data.find("  ") != -1:
			data = data.replace("  ", " ")

		# Turn data into an array
		data = data.split(" ")

		# Get rid of possible null values
		if data[0] == '':			
			data = data[1:]
		if data[-1] == '':
			data = data[:-1]

		# Covert data to float type
		data = [float(i) for i in data]

		# Sort the data		
		data.sort()

		# Keep copy for future reference
		self.data = data
		return data

	def display(self):
		print(self.data)

	def data(self):
		return self.data

	def histogram(self, data=None):
		if data is not None:
			self.data = self.clean(data)

		print("\nDATA SET SIZE: {}\n".format(len(self.data)))
		print('x\t\tfrequency\t\trf\n=====================================================')
		for i in range(int(min(self.data)), int(max(self.data)) + 1):
			frequency = self.data.count(float(i))
			rf = frequency / len(self.data)
			print('{}:\t\t{}\t\t{}'.format(i, frequency, rf))

	def stemLeaf(self, stemFactor, data=None):
		if data is not None:
			self.data = self.clean(data)

		table = dict()


		for value in self.data:
			key = int(value / stemFactor)
			if key not in table:
				table[key] = list()
			table[key].append(value - (key * stemFactor))

		for key in table:
			print(key, table[key])

		return self.data

def mean(data):
	return sum(data)/len(data)

def median(data):
	size = len(data)
	midpoint = int(size / 2)

	# Check if element count is odd
	if size % 2 != 0:
		median = (data[midpoint] + data[midpoint - 1]) / 2
	else:
		median = data[midpoint]

	return median

# sigma^2 = summation[(value - x_bar)**2]/len(data)
def variance(data):
	
	size = len(data)
	mew = mean(data)
	
	summation = sum([(value - mew)**2 for value in data])
	
	return summation / size