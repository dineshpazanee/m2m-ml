import numpy as np
import pandas as pd


#load the csv fine into pandas
df = pd.read_csv('./car-insurance/car_insurance_claim.csv')

print(df.info())