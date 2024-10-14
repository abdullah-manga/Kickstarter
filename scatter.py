import pandas as pd
import matplotlib.pyplot as plt

# Get data from Power BI
df = 

# Create a scatter plot
plt.figure(figsize=(10, 6))
colors = {'Success': 'green', 'Failure': 'red'}
plt.scatter(df['Number of Backers'], [1]*len(df), c=df['Outcome'].apply(lambda x: colors[x]), s=100)

# Add annotations
for i, row in df.iterrows():
    plt.annotate(row['Project ID'], (row['Number of Backers'], 1), textcoords="offset points", xytext=(0,10), ha='center')

# Set axis labels and title
plt.title('Relationship Between Number of Backers and Project Outcome')
plt.xlabel('Number of Backers')
plt.yticks([])  # Hide y-ticks
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
