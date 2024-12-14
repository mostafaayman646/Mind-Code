import numpy as np
import pandas
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set random seed for reproducibility
np.random.seed(42)

# Number of subjects and groups
num_subjects = 76
num_groups = 4

# Parameters for the distributions
kappa_mean = 1
kappa_std = 0.52  # BoundNormal(1, 0.52)
alpha_i_mean = 0.6
alpha_i_std = 0.12  # N(0.6, 0.12)
alpha_ij_std = 0.22  # N(alpha_i, 0.22)

# Generate kappa values (BoundNormal)
kappa = np.random.normal(kappa_mean, kappa_std, num_subjects)

# Generate alpha_i values (Normal distribution)
alpha_i = np.random.normal(alpha_i_mean, alpha_i_std, num_groups)

# Generate alpha_ij values for each subject in each group
alpha_ij = []
for i in range(num_groups):
    # Generate alpha_ij for each subject in group i, with mean alpha_i
    alpha_ij_group = np.random.normal(alpha_i[i], alpha_ij_std, num_subjects // num_groups)
    alpha_ij.append(alpha_ij_group)

# Flatten the list of alpha_ij values for all subjects
alpha_ij = np.concatenate(alpha_ij)

# Create a DataFrame to store the data
data = pandas.DataFrame({
    'Subject_ID': np.arange(1, num_subjects + 1),
    'Kappa': kappa,
    'Alpha_i': np.repeat(alpha_i, num_subjects // num_groups),
    'Alpha_ij': alpha_ij
})

# Export the data to a CSV file
csv_filename = 'synthetic_data.csv'
data.to_csv(csv_filename, index=False)

# Print the first few rows of the DataFrame to verify
print(data.head())

# Plot distributions of kappa, alpha_i, and alpha_ij
plt.figure(figsize=(12, 6))

# Plot kappa distribution
plt.subplot(1, 3, 1)
plt.hist(kappa, bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of kappa (Diffusion coefficient)")
plt.xlabel("kappa")
plt.ylabel("Frequency")

# Plot alpha_i distribution (group means)
plt.subplot(1, 3, 2)
plt.hist(alpha_i, bins=20, color='lightgreen', edgecolor='black')
plt.title("Distribution of alpha_i (Growth rate for groups)")
plt.xlabel("alpha_i")
plt.ylabel("Frequency")

# Plot alpha_ij distribution (individual values)
plt.subplot(1, 3, 3)
plt.hist(alpha_ij, bins=20, color='salmon', edgecolor='black')
plt.title("Distribution of alpha_ij (Individual growth rate within groups)")
plt.xlabel("alpha_ij")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
