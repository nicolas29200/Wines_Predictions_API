import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor

datafull=pd.read_csv("../datasource/Wines.csv")
data=datafull.drop("Id",axis=1)
data=data.drop_duplicates()

#Select X
X=data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
    'pH', 'sulphates', 'alcohol']]
# Select target
y = data["quality"]
# Separate data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y,train_size=0.8, test_size=0.2,random_state=0)
my_model = XGBRegressor(n_estimators=100,learning_rate=0.05)
my_model.fit(X_train, y_train)
my_model.save_model("modelXGBoost.json")