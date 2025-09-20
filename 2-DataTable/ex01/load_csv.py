import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """takes a path as argument, writes the dimensions of the data set
    and returns it"""

    try:
        df = pd.read_csv(path)

        print("Loading dataset of dimensions", df.shape)
        return df

    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
        return None
