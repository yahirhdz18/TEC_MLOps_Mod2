import os
import sys
import typer
import pandas as pd
from datetime import datetime
from pathlib import Path

from typing import List

def get_existing_lists() -> List[str]:
    r""" Reads all existing lists in directory.

    Returns a list containing all the lists in the data directory. 
    It takes no arguments.

    Returns
    -------
    list
        List of lists in the data directory.
    """
    return os.listdir(PATH_TO_DATA)

def get_list_filename(name:str) -> str:
    r""" Retrieve the filname of a specified list.

    Gets the filename of a list using the name parameter and concatenating '.csv'

    Parameters
    ----------
    name : string
        The name of the list as it will be saved without the extention.

    Returns
    -------
    string
        The name + .csv as the filename.
    """
    return f"{name}.csv"

def get_list_path(name: str) -> str:
    r""" Retrieve the path of a specified list.

    Gets the path of a list using the name parameter and concatenating PATH_TO_DATA + name + '.csv'

    Parameters
    ----------
    name : string
        The name of the list as it will be saved without the extention.

    Returns
    -------
    string
        The PATH_TO_DATA + name + .csv as the list path.
    """
    return f"{PATH_TO_DATA}{get_list_filename(name)}"

def store_list(df:pd.DataFrame, name:str) -> None:
    r""" Stores the list with the given name.

    Store the df as a .csv docuemnt with the given name using the get_list_path() function.

    Parameters
    ----------
    df : pd.DataFrame
        A pandas DataFrame that will be stored as a new list.
    name : string
        The name of the list as it will be saved without the extention.
    
    Returns
    -------
    None
    """
    df.to_csv(get_list_path(name), index=False)

def create_list(name:str) -> None:
    r""" Creates a new lsit and stores it in directory.

    It creates a new empty pandas DataFrame with the columns
    'created', 'task', 'summary', 'status', 'owner' and then stores
    it as a list in the directory with the function store_list().

    Parameters
    ----------
    name : string
        The name of the list as it will be saved without the extention.

    Returns
    -------
    None
    """
    df = pd.DataFrame(columns=["created", "task", "summary", "status", "owner"])
    store_list(df, name)

def check_list_exists(name:str) -> bool:
    r""" Checks if the list was already exists.

    Gets the filename of the list using the get_list_filename() function with 
    name as its parameter. Then, check if the list filename is in the existing
    list of lists, using the get_existing_lists() function.

    Parameters
    ----------
    name : string
        The name of the list as it will be saved without the extention.

    Returns
    -------
    bool
        True if the list already exists, False if not.
    """
    return get_list_filename(name) in get_existing_lists()

def load_list(name:str) -> pd.DataFrame:
    r""" Loads csv from directory as a pandas DataFrame.

    Loads a csv file that matches the name from the data directory 
    using the get_list_path() function

    Parameters
    ----------
    name : string
        The name of the list as it will be saved without the extention.

    Returns
    -------
    pd.DataFrame
        A DataFrame of the csv containing the todo list.
    """
    return pd.read_csv(get_list_path(name))

def add_to_list(list_name:str, new_row)->None:
    df = load_list(list_name)
    df.loc[len(df.index)] = new_row
    store_list(df, list_name)

if __name__ == "__main__":
    get_existing_lists()