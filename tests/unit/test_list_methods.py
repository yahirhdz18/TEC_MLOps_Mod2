import sys

import shutil
from datetime import datetime
import pandas as pd
import pytest

sys.path.append('../') 

from tec_mlops_mod2.todos.list_methods import PATH_TO_DATA
from tec_mlops_mod2.todos.list_methods import get_list_path
from tec_mlops_mod2.todos.list_methods import get_list_filename
from tec_mlops_mod2.todos.list_methods import create_list
from tec_mlops_mod2.todos.list_methods import load_list
from tec_mlops_mod2.todos.list_methods import store_list
from tec_mlops_mod2.todos.list_methods import check_list_exists
from tec_mlops_mod2.todos.list_methods import add_to_list
from tec_mlops_mod2.todos.list_methods import update_task_in_list

@pytest.fixture(scope="function")
def tmp_dir(tmpdir_factory):
    my_tmpdir = tmpdir_factory.mktemp("pytestdata")
    PATH_TO_DATA = my_tmpdir
    yield my_tmpdir
    shutil.rmtree(str(my_tmpdir))

@pytest.fixture(scope="session")
def df_empty():
    return pd.DataFrame(columns=["created", "task", "summary", "status", "owner"])

@pytest.fixture(scope="session")
def df_full(new_row):
    return pd.DataFrame(
        [new_row], columns=["created", "task", "summary", "status", "owner"]
    )

@pytest.fixture(scope="function")
def df_full_stored(tmp_dir, df_full):
    df_full.to_csv(f"{tmp_dir}/todos.csv")
    return df_full

@pytest.fixture(scope="function")
def df_empty_stored(tmp_dir, df_empty):
    df_empty.to_csv(f"{tmp_dir}/todos.csv")
    return df_empty

@pytest.fixture(scope="session")
def new_row():
    return {
        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "task": "cocinar",
        "summary": "Cocinar algo rico",
        "status": "todo",
        "owner": "Andre",
    }

def test_get_list_path():
    assert get_list_path("todos") == PATH_TO_DATA + "todos.csv"

def test_get_filename():
    assert get_list_filename("data") == "data.csv"

def test_create_list(tmp_dir, df_empty):
    create_list("todos")
    df1 = load_list("todos")
    pd.testing.assert_frame_equal(df1, df_empty)

def test_store_list(tmp_dir, df_empty):
    store_list(df_empty, "todos")
    df2 = load_list("todos")
    pd.testing.assert_frame_equal(df_empty, df2)

@pytest.mark.xfail
def test_check_list_exists_fail(tmp_dir):
    assert check_list_exists("todos") == False

def test_check_list_exists(df_empty_stored):
    assert check_list_exists("todos") == True

def test_load_list(df_empty_stored, tmp_dir):
    df = load_list("todos")
    pd.testing.assert_frame_equal(df_empty_stored, df)

def test_add_to_list(new_row, df_full, tmp_dir):
    add_to_list("todos", new_row)
    df1 = load_list("todos")
    pd.testing.assert_frame_equal(df1, df_full)

def test_update_list(df_full_stored):
    df_full_stored.loc[0, "owner"] = "Ivan"
    update_task_in_list("todos", 0, "owner", "Ivan")
    df = load_list("todos")
    pd.testing.assert_frame_equal(df, df_full_stored)