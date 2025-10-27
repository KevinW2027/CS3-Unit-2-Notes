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
print(pokemon_df['Name'])
print(pokemon_df.HP)
print(pokemon_df['Type 1'])
#Fill value with calculation
pokemon_df['Attack Ratio'] = pokemon_df['Attack'] / pokemon_df['Sp. Atk']

print(pokemon_df.head()) # Show first n rows
print(pokemon_df.sample(3))
print(pokemon_df.shape)
print(pokemon_df.columns) # list of column headers
print(pokemon_df.info()) # shows non_null count & dtypes
print(pokemon_df.describe())

print(pokemon_df['Type 1'].value_counts())#frequency of value counts
print(pokemon_df.loc[4])
#groupby function helps you isolate group of entries
print(pokemon_df.groupby('Type 1')[['HP','Speed']].mean() )
print( pokemon_df.groupby('Type 1').size().sort_values(ascending=False))
# Create new column with a sum of stat values
pokemon_df['Total'] = pokemon_df [['HP','Attack','Defense','Speed']].sum(axis=1)
print(pokemon_df['Total'])
# Use groupby to identify average total stats by generation
print(pokemon_df.groupby('Generation')['Total'].mean())
# Looks at average total stats for legs
print(pokemon_df.groupby('Legendary')['Total'].mean())
#Select pokemon with high HP values
subset1 = pokemon_df[(pokemon_df['HP'] > 100)]
print(subset1)
# Psychic only
subset2 = pokemon_df[ (pokemon_df['Type 1'] == 'Psychic')]
#Multiple conditions
subset3 = subset2[(subset2['Type 2'] == 'Fairy') & subset2['Sp. Atk'] > 50]
#Name contains Mega
subset4 = pokemon_df[pokemon_df['Name'].str.contains('Mega')]
#Exclude legs
subset5 = pokemon_df[ pokemon_df['Legendary'] == False]
#shortcut with '~'
subset6 = pokemon_df[~pokemon_df['Legendary']]     