import pandas as pd

from utils import add_zero
from utils import fix_colnames
from config import Config

def process_date(df: pd.DataFrame):
    """
    This function aims to build the date variable with the format %Y-%m-%d %H:%M
    
    Arguments
    ---------
    df (pd.DataFrame): raw data
    
    Return
    ------
    data (pd.DataFrame): data with date processed
    """
    
    data = df.copy()
    
    # Build date column: format Y-m-d H:m
    data["month"] = data["month"].apply(add_zero)
    data["day"]   = data["day"].apply(add_zero)
    data["hour"]  = data["hour"].apply(add_zero)

    date_str = (
        data["year"].astype(str) + "-" + 
        data["month"] + "-" + 
        data["day"] + " " + 
        data["hour"] + ":00"
    )
    data["date"] = pd.to_datetime(date_str)
    data["day_name"] = data["date"].dt.strftime("%a")
    data = data.drop(columns = ["year", "month", "day"])
    
    return data

def process_data(df: pd.DataFrame):
    """
    This function aims to process the raw data
    
    Arguments
    ---------
    df (pd.DataFrame): raw data
    
    Return
    ------
    data (pd.DataFrame): data processed    
    """    
    data = df.copy()
    
    data.columns = fix_colnames(data.columns)
    data = process_date(data)    
    
    data = data.dropna(subset=["pm2_5"])
    
    # cbwd has these categories: SE, NW, NE and cv
    # we can suppose that cv is SW
    data["cbwd"] = data["cbwd"].replace({"cv": "SW"})

    # drop useless columns
    cols_drop = ["no"]
    data = data.drop(columns=cols_drop)
    
    data = data.set_index("date")
    
    return data

df = pd.read_csv(Config.INPUT_PATH)
df_prd = process_data(df)

# save dataset

