import os
import sys
import typer
import pandas as pd
from datetime import datetime
from pathlib import Path






def get_existing_lists() -> list:
    return os.listdir(PATH_TO_DATA)

if __name__ == "__main__":
    get_existing_lists()