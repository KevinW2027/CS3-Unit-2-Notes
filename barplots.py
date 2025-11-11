import pandas as pd
from matplotlib import pyplot as plt

# Data
languages = {
    'lang':['Spanish','French','Mandarin','English'],
    'speaker':[5,2,2,8],
    'difficulty':[ 6, 8, 0, 2]
    }
df = pd.DataFrame(languages)
colors=['blue','yellow','green','red']
df_sorted = df.sort_values(by='speaker',ascending=False)
plt.bar(df_sorted['lang'],df_sorted['speaker'],color=colors,width=0.6)

#often need to rotate labels on x axis for readability
plt.xticks(rotation=45)
plt.xlabel('language')
plt.ylabel('Count of Speaker')
plt.title('Speakers for each languge')
plt.savefig('barchart.png', bbox_inches='tight')
plt.close()

# Pie charts - to show parts of a whole/breakdown of a total
plt.pie(df['speaker'],labels=df['lang'].tolist(),startangle=270)
plt.title('Speaker of each language')
plt.savefig('piecharts.png',bbox_inches='tight')

