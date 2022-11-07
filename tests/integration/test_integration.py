import sys
import os
import shutil

from datetime import datetime
import pandas as pd

import pytest
from typer.testing import CliRunner

sys.path.append('./') 

from tec_mlops_mod2.todos.list_methods import PATH_TO_DATA
from tec_mlops_mod2.todos.list_methods import load_list
from tec_mlops_mod2.main import app

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
        "task": "Cook",
        "summary": "Cook something tasty",
        "status": "todo",
        "owner": "Yahir"
    }

runner = CliRunner()

def test_create_and_check(df_empty):
    result_create = runner.invoke(app, ["create", "-ln", "todos"])
    assert result_create.exit_code == 0
    df1 = load_list("todos")
    pd.testing.assert_frame_equal(df1, df_empty)

    result_list = runner.invoke(app, ["list"])
    assert result_list.exit_code == 0

    result_show = runner.invoke(app, ["show", "-ln", "todos"])
    assert result_show.exit_code == 1

def test_add_and_update(new_row):
    result_add = runner.invoke(app, ["add", "-ln", "todos", "-tn", "Cook",\
        "-d", "Cook something tasty", "-o", "Yahir"])

    assert result_add.exit_code == 0
    df1 = load_list("todos")
    df1_first_row = list(df1.iloc[0])
    new_row_list = list(new_row.values())
    assert df1_first_row[1:] == new_row_list[1:]
    

    result_update = runner.invoke(app, ["update", "-ln", "todos", "-i", 0, "-f", "status", "-c", "in_progress"])
    assert result_update.exit_code == 0
    df1 = load_list("todos")
    df1_first_row = list(df1.iloc[0])
    new_row_list[3] = "in_progress"
    assert df1_first_row[1:] == new_row_list[1:]
    os.remove(f"{PATH_TO_DATA}/todos.csv") 
