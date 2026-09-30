import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate Traffic Accident Dataset Structure
np.random.seed(42)
n = 1500

df = pd.DataFrame({
    'Hour': np.random.randint(0, 24, size=n),
    'Weather': np.random.choice(['Clear', 'Rain', 'Fog', 'Snow'], size=n, p=[0.6, 0.25, 0.1, 0.05]),
    'Road_Condition': np.random.choice(['Dry', 'Wet', 'Icy'], size=n, p=[0.65, 0.28, 0.07]),
    'Severity': np.random.choice([1, 2, 3, 4], size=n, p=[0.1, 0.5, 0.3, 0.1])
})

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 1. Accidents by Hour of Day
sns.histplot(df['Hour'], bins=24, kde=True, ax=axes[0], color='crimson')
axes[0].set_title('Accidents Frequency by Hour of Day', fontsize=14)
axes[0].set_xlabel('Hour (0-23)')
axes[0].set_ylabel('Accident Count')

# 2. Accidents by Weather & Road Conditions
sns.countplot(data=df, x='Weather', hue='Road_Condition', ax=axes[1], palette='magma')
axes[1].set_title('Accidents by Weather & Road Conditions', fontsize=14)
axes[1].set_xlabel('Weather Condition')
axes[1].set_ylabel('Accident Count')

plt.tight_layout()
plt.savefig('accident_patterns.png')
plt.show()

print("Task 5 Completed successfully.")
