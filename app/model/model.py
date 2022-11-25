import pandas as pd
from sklearn import model_selection,metrics
from xgboost import XGBRegressor
from csv import DictWriter
import os

def data_X_y():
    datafull=pd.read_csv("app/datasource/Wines.csv",header=0,index_col="Id")
    data=datafull.drop_duplicates()

    #Select X
    X=data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
        'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
        'pH', 'sulphates', 'alcohol']]
    # Select target
    y = data["quality"]
    return X,y
def Data_separation(X,y):
    X_train, X_valid, y_train, y_valid = model_selection.train_test_split(X, y,train_size=0.8, test_size=0.2,random_state=0)
    return [X_train, X_valid, y_train, y_valid]
def save_model():
    X,y=data_X_y()
    # Separate data into training and validation sets
    Xy_Train_Test = Data_separation(X,y)
    X_train,y_train=Xy_Train_Test[0],Xy_Train_Test[2]
    my_model = XGBRegressor(n_estimators=100,learning_rate=0.05)
    my_model.fit(X_train, y_train)
    my_model.save_model("app/model/modelXGBoost.json")

def load_Model(my_model):
    if os.path.isfile("app/model/modelXGBoost.json"):
        my_model.load_model("app/model/modelXGBoost.json")

    else:
        save_model()
        my_model.load_model("app/model/modelXGBoost.json")
    return my_model


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

def description():
    X,y=data_X_y()
    # Separate data into training and validation sets
    n_estimators=100
    learning_rate=0.05
    X_train, X_valid, y_train, y_valid = model_selection.train_test_split(X, y,train_size=0.8, test_size=0.2,random_state=0)
    model_xgb= XGBRegressor(n_estimators,learning_rate)
    model_xgb.load_model("app/model/modelXGBoost.json")
    predictions = list(map(round,model_xgb.predict(X_valid)))
    return {"n_estimators":n_estimators,"learning_rate":learning_rate,"mean_absolute_error":metrics.mean_absolute_error(predictions, y_valid)}


def prediction(wine):
    my_model=XGBRegressor(n_estimators=100,learning_rate=0.05)
    my_model=load_Model(my_model)
    resultat=my_model.predict(wine)
    return resultat