import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from chart_lib import Chart_lib


#load the csv fine into pandas
pd.set_option('display.max_columns', None)
df = pd.read_csv('./car-insurance/insurance_claims.csv')
clib = Chart_lib()

gender_counts = df['insured_sex'].value_counts()
clib.pie_chart(gender_counts, 'Gender Distribution')

genuine_incident = df[df['fraud_reported'] == 'N']
clib.pie_chart(genuine_incident['insured_sex'].value_counts(), 'Gender Distribution from true Incident')
