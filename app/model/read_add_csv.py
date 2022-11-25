import pandas as pd


def read_CSV(path) -> pd.DataFrame:
    df =  pd.read_csv(path, header=0, index_col="Id")
    return df
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


    """
    def writeNewWine(self, 
                    fixedAcidity : float, volatileAcidity : float, 
                    citricAcid : float, residualSugar : float, 
                    chlorides : float, freeSulfurDioxyde : float,
                    totalSulfurDioxyde : float, density : float,
                    pH : float, sulphates : float, 
                    alcohol : float, quality : int):
        
        # Get last index
        with open(self.path, 'r') as f:
            lastLine = f.readlines()[-1]
            lastIndex = lastLine.split(',')[-1]

        newEntry = pd.DataFrame([[fixedAcidity, volatileAcidity, citricAcid,
                                residualSugar, chlorides, freeSulfurDioxyde,
                                totalSulfurDioxyde, density, pH, sulphates,
                                alcohol, quality, (lastIndex +1)]])

        print(newEntry.to_string())

        newEntry.to_csv(self.path, header=0, index=False, mode='a')"""