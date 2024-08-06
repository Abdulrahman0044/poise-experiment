from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import pandas as pd

# Load the trained model
model = load_model('flow_rate.h5')

# Load the data
data = pd.read_csv(r'.\PoiseExperiment\data\evaluation_fluid_flow_data.csv')

# Assume 'scaler' is the scaler used during training
scaler = StandardScaler()
new_data_scaled = scaler.fit_transform(data)

# Predict flow rates
predicted_flow_rates = model.predict(new_data_scaled)

# Add predictions to the DataFrame
data['predicted_Q'] = predicted_flow_rates

print(data)

# Visualize predicted flow rates
plt.scatter(range(4000), data['predicted_Q'])
plt.xlabel('Sample')
plt.ylabel('Predicted Flow Rate (Q)')
plt.title('Predicted Flow Rates for 4000 Parameters')
plt.show()
plt.savefig('image.png')


