import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()


# Define the number of samples
num_samples = 10

# Generate random values within reasonable ranges
radii = [fake.random.uniform(0.0001, 0.01) for _ in range(num_samples)]  # pipe radius in meters
lengths = [fake.random.uniform(0.1, 10) for _ in range(num_samples)]     # pipe length in meters
viscosities = [fake.random.uniform(0.001, 0.01) for _ in range(num_samples)] # dynamic viscosity in Pa.s
pressures = [fake.random.uniform(100, 10000) for _ in range(num_samples)]    # pressure drop in Pascals

# Calculate the flow rate 
# flow_rates = [(delta_P * np.pi * r**4) / (8 * mu * L) for delta_P, r, mu, L in zip(pressures, radii, viscosities, lengths)]

# Create a DataFrame
data = pd.DataFrame({
    'delta_P (pa)': pressures,
    'r (m)': radii,
    'mu (Pa.s)': viscosities,
    'L (m)': lengths,
})

# Save dataset to a CSV file
data.to_csv('evaluation_fluid_flow_data.csv', index=False)

print(data.head())