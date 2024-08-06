import pandas as pd
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv(r'.\PoiseExperiment\data\synthetic_fluid_flow_data.csv')
X = data[['delta_P', 'r', 'mu', 'L']].values
y = data['Q'].values

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Set tensorflow oneDNN to 0
os.environ["TF_ENABLE_ONEDNN_OPTS"] = '0'

# Define the neural network model
model = Sequential([
    Dense(64, input_dim=4, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1, activation='linear')
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)

# Save the model
model.save('flow_rate.h5')