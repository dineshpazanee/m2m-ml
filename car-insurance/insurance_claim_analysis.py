import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#load the csv fine into pandas
pd.set_option('display.max_columns', None)
df = pd.read_csv('./car-insurance/insurance_claims.csv')

gender_counts = df['insured_sex'].value_counts()

gender_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightpink'])

# Add a title
plt.title('Gender Distribution')

# Display the pie chart
plt.show()