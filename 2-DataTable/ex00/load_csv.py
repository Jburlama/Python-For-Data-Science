import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    try:
        df = pd.read_csv(path)

        print("Loading dataset of dimensions", df.shape)
        return df

    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
        return None
