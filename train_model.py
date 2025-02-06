import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Step 1: Load the dataset
data = pd.read_csv('train.csv')  # Replace 'train.csv' with the actual file path

# Step 2: Preprocess the data
X = data.drop(columns=['SalePrice'])  # Replace 'SalePrice' with the target column name
y = data['SalePrice']

# Handle missing values
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

numerical_imputer = SimpleImputer(strategy='mean')
X[numerical_features] = numerical_imputer.fit_transform(X[numerical_features])

# Encode categorical variables
X = pd.get_dummies(X, columns=categorical_features, drop_first=True)

# Scale numerical features
scaler = StandardScaler()
X[numerical_features] = scaler.fit_transform(X[numerical_features])

# Step 3: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model
import joblib
joblib.dump(model, 'house_price_model.pkl')