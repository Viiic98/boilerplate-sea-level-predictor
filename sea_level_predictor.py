import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    plt.figure(figsize=(13,6))
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)
    # Create first line of best fit
    res1 = linregress(x, y)
    xx1 = list(range(1880, 2051))
    yy1 = [res1.intercept + res1.slope * year for year in xx1]
    plt.plot(xx1, yy1, 'r', label='Best Line 1')

    # Create second line of best fit
    x2 = df['Year'][df['Year'] >= 2000]
    y2 = df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000]
    res2 = linregress(x2, y2)
    xx2 = list(range(2000, 2051))
    yy2 = [res2.intercept + res2.slope * year for year in xx2]
    plt.plot(xx2, yy2, 'g', label='Best Line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()