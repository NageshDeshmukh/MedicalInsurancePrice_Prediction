## Project Overview

The goal of this project is to predict medical insurance premiums based on various independent features such as age, gender, BMI, number of children, smoking status, and region. The prediction model helps insurance companies and individuals estimate the cost of medical insurance, enabling better financial planning and decision-making.

## Technologies Used

## Programming Language: Python

## Libraries and Frameworks:

## Data Manipulation and Analysis: Pandas, NumPy

## Data Visualization: Matplotlib, Seaborn

## Machine Learning: Scikit-learn, Statsmodels

## Model Evaluation: Mean Squared Error (MSE), Mean Absolute Error (MAE), R² Score, Adjusted R² Score

## Feature Engineering: One-Hot Encoding, Variance Inflation Factor (VIF)

## Regularization Techniques: Ridge Regression, Lasso Regression

## Hyperparameter Tuning: GridSearchCV, RandomizedSearchCV

## Model Serialization: Pickle

## Web Framework: Flask (for deployment)

## Tools: Jupyter Notebook, VS Code

## Data Source: Medical Insurance Dataset (CSV file)

### Key Steps and Methodology

## 1. Data Gathering:

Loaded the dataset using Pandas and performed initial data exploration.

## 2. Exploratory Data Analysis (EDA):

Checked for missing values and outliers.

Visualized data distributions and correlations using boxplots, heatmaps, and scatterplots.

Detected outliers using IQR and Z-score methods.

## 3. Feature Engineering:

Encoded categorical variables (gender, smoker, region) using label encoding and one-hot encoding.

Renamed columns for better readability.

Handled missing values and outliers.

## 4. Feature Selection:

Calculated Variance Inflation Factor (VIF) to check for multicollinearity.

Analyzed correlation matrices to identify significant features.

## 5. Model Selection:

Split the data into training and testing sets.

Implemented Linear Regression, Ridge Regression, and Lasso Regression models.

Evaluated models using MSE, MAE, R² Score, and Adjusted R² Score.

## 6. Hyperparameter Tuning:

Used GridSearchCV and RandomizedSearchCV to optimize hyperparameters for Ridge and Lasso Regression.

7. Model Evaluation:

Compared the performance of Linear Regression, Ridge Regression, and Lasso Regression.

Selected the best model based on evaluation metrics.

## 8. Model Deployment:

Serialized the final model using Pickle.

Created a Flask API to predict insurance premiums based on user inputs.

Deployed the model locally using Flask.

Results

Achieved an R² score of 0.694 and an Adjusted R² score of 0.684 on the test dataset using the Linear Regression model.

Ridge and Lasso Regression models showed similar performance, with slight improvements in certain cases after hyperparameter tuning.

The final model was deployed using Flask, allowing users to input their details and receive a predicted insurance premium.
# Regularization 
# HyperParameter Tunning
# API Writing And Testing
# Final Mediacl_Insurance_Price_Prediction
