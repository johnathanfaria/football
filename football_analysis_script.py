
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
data = {
    'Player': ['Messi', 'Ronaldo', 'Neymar', 'Lewandowski', 'Suarez', 'Kane'],
    'Goals': [750, 900, 400, 600, 500, 300],
    'Assists': [300, 200, 250, 200, 200, 150],
    'Ratio': [1.05, 0.85, 0.83, 0.86, 0.80, 0.71],
    'Games': [1000, 1100, 650, 930, 850, 600]
}

df = pd.DataFrame(data)

# Sorting the dataframe by 'Goals + Assists per Game' in descending order
df['Goals + Assists'] = df['Goals'] + df['Assists']
df_sorted_by_sum = df.sort_values(by='Goals + Assists', ascending=False)

# Plotting stacked Goals and Assists with Ratio as a line
fig, ax1 = plt.subplots(figsize=(10, 8))

bars_goals = ax1.barh(df_sorted_by_sum['Player'], df_sorted_by_sum['Goals'], color='blue', label='Goals', alpha=0.7)
bars_assists = ax1.barh(df_sorted_by_sum['Player'], df_sorted_by_sum['Assists'], left=df_sorted_by_sum['Goals'], color='green', label='Assists', alpha=0.7)

for bar in bars_goals:
    ax1.text(bar.get_width() - 10, bar.get_y() + bar.get_height() / 2, f'{int(bar.get_width())}', va='center', ha='right', color='white', fontweight='bold')

for bar in bars_assists:
    ax1.text(bar.get_x() + bar.get_width() - 10, bar.get_y() + bar.get_height() / 2, f'{int(bar.get_width())}', va='center', ha='right', color='white', fontweight='bold')

ax2 = ax1.twiny()
ax2.set_xlim(0, 1.2)
bar_bottom_positions = [bar.get_y() for bar in bars_goals]
ax2.plot(df_sorted_by_sum['Ratio'], bar_bottom_positions, color='red', marker='o', label='Ratio', linewidth=2)

ax2.grid(False)
ax2.set_xlabel("Ratio (Goals + Assists per Game)")
ax1.set_title("Total Goals and Assists per Player with Ratio")
ax1.legend()
plt.tight_layout()
plt.show()

# Plotting Ratio Distribution
bins = [0.6, 0.8, 1.0, float('inf')]
labels = ['0.6 - 0.8', '0.8 - 1.0', '> 1.0']
df['Ratio Category'] = pd.cut(df['Ratio'], bins=bins, labels=labels, right=False)
ratio_distribution = df['Ratio Category'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8, 6))
ratio_distribution.plot(kind='bar', color=['blue', 'green', 'red'], ax=ax)
ax.set_xlabel("Ratio Category")
ax.set_ylabel("Number of Players")
ax.set_title("Distribution of Players Based on Ratio (Goals + Assists per Game)")
plt.tight_layout()
plt.show()

# Plotting Histogram of Ratio
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(df['Ratio'], bins=np.arange(0.5, 1.25, 0.1), color='blue', edgecolor='black')
ax.set_xlabel("Ratio (Goals + Assists per Game)")
ax.set_ylabel("Number of Players")
ax.set_title("Histogram of Ratio (Goals + Assists per Game) with 0.1 Intervals")
ax.set_xticks(np.arange(0.5, 1.25, 0.1))
ax.set_xticklabels([f'{tick:.1f}' for tick in np.arange(0.5, 1.25, 0.1)])
plt.tight_layout()
plt.show()
