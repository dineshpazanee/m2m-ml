#https://data.mendeley.com/datasets/992mh7dk9y/2
#https://www.kaggle.com/datasets/litvinenko630/insurance-claims

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from chart_lib import Chart_lib
from utils import Date_utils


#load the csv fine into pandas
pd.set_option('display.max_columns', None)
df = pd.read_csv('./car-insurance/Car_Insurance_Claims.csv')
clib = Chart_lib()
date_util = Date_utils()
#print(df.info())

gender_counts = df['gender'].value_counts()
#clib.pie_chart(gender_counts, 'Gender Distribution')

df['is_legal_age'] = df['birthdate'].apply(date_util.cal_leagl_age)
legal_age = df['is_legal_age'].value_counts()
clib.pie_chart(legal_age, 'Group by Age')

#obj = date_util.convertMDYYYY('4/21/1986')
#legal_age = date_util.getLegalAge(obj)
#is_legal = date_util.isLegalAge(legal_age.year, 2024)
#print(obj)
#print(legal_age)
#print(is_legal)

#claimed = df[df['OUTCOME'] == 1.0]
#claimed_by_age = claimed['AGE'].value_counts()
#clib.bar_chart(claimed_by_age, 'Insurance Claimed by age')

#driving_exprience = claimed['DRIVING_EXPERIENCE'].value_counts()
#clib.bar_chart(driving_exprience, 'Claimed by Driving Exprience')

#credit_score = df['POSTAL_CODE'].value_counts()
#print(credit_score)

