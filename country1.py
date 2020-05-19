import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']	names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]	dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]	cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)


# Import pandas as pd	# Definition of row_labels

row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
import pandas as pd	
# Create dictionary my_dict with three key:value pairs: my_dict	
my_dict={'country':names,'drives_right':dr,'cars_per_cap':cpc}	


# Build a DataFrame cars from my_dict: cars	# Specify row labels of cars
cars=pd.DataFrame(my_dict)	cars.index=row_labels


# Print cars	# Print cars again
print(cars)	print (cars)
