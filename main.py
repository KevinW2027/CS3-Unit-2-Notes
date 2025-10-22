import numpy as np
import pandas as pd

# Series object is a 1D array of indexed data
# Single column (One catagory)

months = pd.Series(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
print(months)
# Series have attributes
print(months.values) # Looks like a list
print(months.index) # Can set the index explicitly 

month_list = pd.Series(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
#better_month = pd.Series([month_list], index = [1,2,3,4,5,6,7,8,9,10,11,12])

# Access value at index
#print(f'My birthday is in {better_month[3]}')
birth_months = {'Kevin':'Mar',
                'Jackson': 'Aug',
                'Finny':'Jul',
                'Bryce':'Nov',
                'Natalie':'Mar',
                'Paige':'Feb',
                'Maia':'Apr'}
birth_series = pd.Series(birth_months)
print(birth_series)

# Create a single Dataframe from a single Series object

df = pd.DataFrame(birth_series, columns=['Birth months'])
print(df) #Has column headings

# Load tabular data from a csv file into a dataframe
pokemon_df = pd.read_csv('pokemon_data.csv')
print(pokemon_df.columns)
print(pokemon_df['Name'])