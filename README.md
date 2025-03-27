# Electricity Consumption Prediction using Linear Regression

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
  
## Introduction

This project implements a **Linear Regression Model from scratch** to predict electricity consumption and bill amounts based on past data. Unlike traditional machine learning libraries, the model is built using fundamental statistical methods.

## Features

- **Manual Data Collection**: The dataset was collected from personal electricity bills over the past year.
- **Custom Linear Regression Implementation**: No pre-built ML libraries like scikit-learn were used.
- **Visualization**: Graphs showing actual vs. predicted consumption trends.
- **Future Prediction**: Estimates electricity usage for upcoming months.

## Dataset

The dataset consists of:
- **Months (1-12)** representing past electricity usage.
- **Electricity Usage (kWh)** recorded each month.
- **Bill Amount (Currency)** corresponding to the usage.

If you want to use a dynamically loaded dataset from an Excel file, use **pandas**:

```python
import pandas as pd

# Read Excel file
df = pd.read_excel('electricity_data.xlsx')

# Extract required columns
months = df['Month'].values
usage_kwh = df['Usage_kWh'].values
bill_amount = df['Bill_Amount'].values
```

Ensure pandas is installed:
```bash
pip install pandas openpyxl
```

## Technologies Used

- **Python**
- **NumPy** (for numerical operations)
- **Matplotlib** (for visualization)
- **Pandas** (for optional Excel file support)

## Project Structure

```bash
.
├── data
│   ├── electricity_data.xlsx  # (Optional Excel file for dynamic input)
├── linear_regression.py       # Main script implementing the model
├── README.md
```

## Setup and Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/Electricity-Consumption-Prediction.git
   cd Electricity-Consumption-Prediction
   ```

2. **Install dependencies:**
   ```sh
   pip install numpy matplotlib pandas openpyxl
   ```

3. **Run the project:**
   ```sh
   python linear_regression.py
   ```

## Usage

1. **Training the model:**
   - The script reads the dataset and fits a linear regression model.
2. **Predicting consumption:**
   - Uses the trained model to forecast electricity consumption for future months.
3. **Visualizing results:**
   - Generates plots for actual vs. predicted values.

## Future Improvements

- Extend dataset with factors like temperature and appliance usage.
- Implement advanced regression models for better accuracy.
- Deploy as a web application.


