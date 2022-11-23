import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from csv import DictWriter

def save_model():
    datafull=pd.read_csv("app/datasource/Wines.csv")
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
    my_model.save_model("app/model/modelXGBoost.json")

def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)

def add_data(row_dict):
    field_names=list(row_dict.keys())
    append_dict_as_row('app/datasource/Wines.csv', row_dict, field_names)

#dicto={"fixed acidity":0,"volatile acidity":0,"citric acid":0,"residual sugar":0,"chlorides":0,"free sulfur dioxide":0,"total sulfur dioxide":0,"density":0,"pH":0,"sulphates":0,"alcohol":0,"quality":0,"Id":0}
