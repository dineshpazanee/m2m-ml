import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Chart_lib:
    
    def __init__(self):
        self.colors = ['salmon','orange', 'lightblue', 'lightgreen']
        pass
    
    
    def pie_chart(self, data, title):
        data.plot.pie(autopct='%1.1f%%', startangle=90, colors=self.colors)
        plt.title(title)
        plt.show()

    def bar_chart(self, data, title):
        
        data.plot(kind='bar', color=self.colors, edgecolor='black')
        plt.title(title)
        plt.ylabel('Count')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    def line_chart(self, data, title):
        
        data.set_index('Year', inplace=True)

        # Plot multiple line chart
        data.plot(kind='line', marker='o', figsize=(8, 5))

        # Customize the chart
        plt.title('State-wise Growth Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.legend(title='States')
        plt.grid(True, linestyle='--', alpha=0.7)

        # Show the plot
        plt.show()