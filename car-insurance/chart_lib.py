import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Chart_lib:
    
    def __init__(self):
        pass
    
    
    def pie_chart(self, data, title):
        data.plot.pie(autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightpink'])
        plt.title(title)
        plt.show()