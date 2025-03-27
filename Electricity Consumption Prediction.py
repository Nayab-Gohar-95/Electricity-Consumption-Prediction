import numpy as np
import matplotlib.pyplot as plt

# Extracted Data
months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # Representing months as numbers
usage_kwh = np.array([144, 18, 23, 26, 40, 411, 474, 533, 439, 305, 177, 134])  # Electricity usage in kWh
bill_amount = np.array([25641, 695, 1221, 510, 645, 20988, 50443, 61826, 82726, 99966, 56758, 37405])  # Bill in currency

# Function to calculate Linear Regression manually
def linear_regression(x, y):
    n = len(x)
    mean_x, mean_y = np.mean(x), np.mean(y)
    
    # Calculating slope (m) and intercept (b)s
    num = sum((x - mean_x) * (y - mean_y))
    den = sum((x - mean_x) ** 2)
    m = num / den
    b = mean_y - (m * mean_x)
    
    return m, b

# Train the model for electricity usage prediction
m_usage, b_usage = linear_regression(months, usage_kwh)

# Train the model for bill amount prediction
m_bill, b_bill = linear_regression(usage_kwh, bill_amount)

# Predict future values
future_months = np.array([13, 14, 15])  # Forecasting next 3 months (Feb, Mar, Apr 2025)
predicted_usage = m_usage * future_months + b_usage
predicted_bill = m_bill * predicted_usage + b_bill

# Plot results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(months, usage_kwh, color='blue', label='Actual Data')
plt.plot(future_months, predicted_usage, color='red', linestyle='dashed', label='Prediction')
plt.xlabel('Month')
plt.ylabel('Electricity Usage (kWh)')
plt.legend()
plt.title('Electricity Usage Prediction')

plt.subplot(1, 2, 2)
plt.scatter(usage_kwh, bill_amount, color='green', label='Actual Data')
plt.plot(predicted_usage, predicted_bill, color='orange', linestyle='dashed', label='Prediction')
plt.xlabel('Electricity Usage (kWh)')
plt.ylabel('Total Bill (Currency)')
plt.legend()
plt.title('Bill Prediction')

plt.show()

# Display Predictions
for i in range(len(future_months)):
    print(f'Month {future_months[i]}: Predicted Usage = {predicted_usage[i]:.2f} kWh, Predicted Bill = {predicted_bill[i]:.2f}')
