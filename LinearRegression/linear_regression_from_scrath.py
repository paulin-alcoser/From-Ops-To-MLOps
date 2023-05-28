import pandas as pd
import numpy as np
from typing import List


def load_data(filename, columns: List[str]]):
    df = pd.read_csv(filename)
    set_columns(df, columns)
    data = np.array(df, dtype=float)

def set_columns(df, columns):
    df.columns = columns
