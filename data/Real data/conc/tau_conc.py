import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the tau concentration ranges (in pg/ml for CSF)
tau_ranges = {
    'Parietal Lobe': (50, 300),     # Parietal Lobe concentration range
    'Hippocampus': (150, 400),      # Hippocampus concentration range
    'Entorhinal Cortex': (100, 250),# Entorhinal Cortex concentration range
    'Frontal Cortex': (50, 200),    # Frontal Cortex concentration range
    'Temporal Lobe': (150, 350)     # Temporal Lobe concentration range
}

# Number of subjects
n_subjects = 46

# Number of time points (1 to 10 years)
n_years = 10

# Generate synthetic tau concentrations for each subject at each year
subjects = [f"Subject_{i+1}" for i in range(n_subjects)]
years = np.arange(1, n_years + 1)

# List to store the data
data_list = []

# Simulate tau concentration for each subject, year, and region
for subject in subjects:
    for year in years:
        for region, (min_tau, max_tau) in tau_ranges.items():
            # Randomly generate tau concentration within the specified range for each region
            tau_concentration = np.random.uniform(min_tau, max_tau)
            data_list.append({
                'Subject': subject,
                'Year': year,
                'Region': region,
                'Tau_Concentration': tau_concentration
            })

# Convert the list of dictionaries into a DataFrame
tau_data = pd.DataFrame(data_list)

# Display the first few rows of the simulated data
print(tau_data.head())

# Optional: Plot tau concentration trends over time for one subject
subject_example = tau_data[tau_data['Subject'] == 'Subject_1']

# Plot the data
plt.figure(figsize=(10, 6))
for region in tau_ranges.keys():
    region_data = subject_example[subject_example['Region'] == region]
    plt.plot(region_data['Year'], region_data['Tau_Concentration'], label=region)

plt.title('Tau Concentration Trends for Subject_1')
plt.xlabel('Year')
plt.ylabel('Tau Concentration (pg/ml)')
plt.legend()
plt.grid(True)
plt.show()

# Save the generated data to a CSV file
tau_data.to_csv('tau_concentration_data.csv', index=False)
