import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create empty DataFrame
df = pd.DataFrame()

# Define file numbers and base filename
file_numbers = [4, 5, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 22, 23, 24, 25, 27, 28, 31, 32]
base_file_name = 'user_{}th_info.csv'

# Loop through files and read data
for file_number in file_numbers:
  try:
    file_name = base_file_name.format(file_number)
    df = pd.concat([df, pd.read_csv(file_name)], ignore_index=True)  # Concatenate DataFrames
  except FileNotFoundError:
    print(f"File {file_name} not found. Skipping...")

df = pd.read_csv('concatenate_all_files.csv')

# Save the concatenated DataFrame to CSV
df.to_csv("concatenate_all_files.csv", index=False)

df = pd.read_csv('concatenate_all_files.csv')

# Drop the timestamp column
df = df.drop(columns=[df.columns[0]])

# Compute the correlation matrix
correlation_matrix = df.corr()

# Set up the matplotlib figure with a larger size
plt.figure(figsize=(14, 12))

# Draw the heatmap with seaborn
heatmap = sns.heatmap(
    correlation_matrix,
    annot=True,
    annot_kws={"size": 10},  # Adjust the font size of annotations
    cmap='coolwarm',
    fmt='.2f',
    cbar_kws={"shrink": .8}  # Adjust the size of the colorbar
)

# Rotate the x and y axis labels to avoid overlap
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Set the title
plt.title('Correlation Matrix Heatmap', fontsize=16)

# Save the heatmap as a PNG
plt.savefig('correlation_matrix_heatmap.png', bbox_inches='tight', dpi=300)

# Optionally show the heatmap
# plt.show()