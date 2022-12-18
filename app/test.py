import model.read_add_csv as read_add
import pytest
def test_read_CSV():
    """Test la fonction Read_Csv
    """    
    df=read_add.read_CSV("app/datasource/Wines.csv")
    assert(len(df.columns)==12)

def test_add_data():
    """Test la fonction add_data_tocsv
    """    
    new_Wine={"fixed acidity":5,"volatile acidity":5,"citric acid":5,"residual sugar":5,"chlorides":5,"free sulfur dioxide":5,"total sulfur dioxide":5,"density":5,"pH":5,"sulphates":5,"alcohol":5,"quality":5,"Id":4}

    field_names=list(new_Wine.keys())
    read_add.append_dict_as_row("app/tests/test.csv", new_Wine, field_names)
    df=read_add.read_CSV("app/tests/test.csv")
    assert(df.iloc[-1].to_list()==[5,5,5,5,5,5,5,5,5,5,5,5])
