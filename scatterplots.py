import pandas as pd
from matplotlib import pyplot as plt

#read csv file into pandas dataframe
cities = pd.read_csv('california_cities.csv')
print(cities.info())

# Extract data columns form our scatterplot
latitude = cities['latd']
longitude = cities['longd']

population = cities['population_total']
area = cities['area_total_sq_mi']

#Generate Scatterplot (Each city row is a scatterplot)

plt.scatter(longitude, latitude)

plt.savefig('scatter-cities.png')
plt.close