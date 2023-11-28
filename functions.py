
import pandas as pd

def cleaning_column_names(dataframe: pd.DataFrame) ->pd.DataFrame:
    '''
    Cleans and formats the name of the columns.
        
    Inputs:
    dataframe: Pandas DataFrame
    
    Outputs:
    dataframe: Pandas DataFrame
    '''
    dataframe2 = dataframe.copy()
    cols = []
    for col in dataframe2.columns:
        cols.append(col.lower())
    dataframe2.columns = cols
    dataframe2.columns = dataframe2.columns.str.replace(' ', '_')
    dataframe2.rename(columns={"st": "state"}, inplace=True)
    return dataframe2

def cleaning_invalid_values(dataframe:pd.DataFrame)-> pd.DataFrame:
    '''
    Fixes typos and invalid values in the columns of a dataframe.
    Inputs:
    dataframe: pd.DataFrame
    Outputs:
    dataframe: pd.DataFrame
    
    '''
    
    dataframe2 = dataframe.copy()
    dataframe2['gender'] = dataframe2['gender'].replace(['Femal', 'female'], 'F')
    dataframe2['gender'] = dataframe2['gender'].replace(['Male'], 'M')
    dataframe2['state'] = dataframe2['state'].replace(['Cali'], 'California')
    dataframe2['state'] = dataframe2['state'].replace(['AZ'], 'Arizona')
    dataframe2['state'] = dataframe2['state'].replace(['WA'], 'Washington')
    dataframe2['education'] = dataframe2['education'].replace(['Bachelors'], 'Bachelor')
    dataframe2['customer_lifetime_value'] = dataframe2['customer_lifetime_value'].str.replace('%', '')
    dataframe2['vehicle_class'] = dataframe2['vehicle_class'].replace(['Sports Car', 'Luxury SUV', 'Luxury Car'], 'Luxury')
    return dataframe2

def formatting_data_types(dataframe:pd.DataFrame)-> pd.DataFrame:
    '''
    Changes the data types of a pandas Dataframe to the correct format.
    Inputs:
    dataframe: pd.DataFrame
    Outputs:
    dataframe: pd.DataFrame
    
    '''
    
    dataframe2 = dataframe.copy()
    dataframe2["customer_lifetime_value"] = pd.to_numeric(dataframe2["customer_lifetime_value"])
    dataframe2["number_of_open_complaints"] = dataframe2["number_of_open_complaints"].apply(lambda x: str(x).split()[0][2] if len(str(x))==6 else x)
    dataframe2["number_of_open_complaints"] = pd.to_numeric(dataframe2["number_of_open_complaints"])
    return dataframe2

def dealing_with_null_values(dataframe: pd.DataFrame)->pd.DataFrame:   
    '''
    Removes nans from a pandas dataframe.
    Inputs:
    dataframe: Pandas dataFrame
    
    Outputs:
    dataframe2: Pandas dataFrame
    '''
    
    dataframe2 = dataframe.copy()
    dataframe2.dropna(axis=0, how="all",inplace=True)
    dataframe2.reset_index()
    median_customer_lifetime_value = dataframe2['customer_lifetime_value'].median()
    dataframe2['customer_lifetime_value'] = dataframe2['customer_lifetime_value'].fillna(median_customer_lifetime_value)
    dataframe2['gender'] = dataframe2['gender'].fillna("U")
    return dataframe2

def dealing_with_duplicates(dataframe: pd.DataFrame)->pd.DataFrame:   
    '''
    Removes duplicate entries from a pandas dataframe keeping the first one.
    Inputs:
    dataframe: Pandas dataFrame
    
    Outputs:
    dataframe2: Pandas dataFrame
    '''
    
    dataframe2 = dataframe.copy()
    dataframe2.drop_duplicates(keep='first', inplace=True)
    return dataframe2
