"""
utils.py
Helper functions for loading the color dataset.
"""

import pandas as pd


def load_colors(csv_path: str) -> pd.DataFrame:
    """
    Load the colors CSV. Expected columns: color_name, hex, R, G, B
    """
    df = pd.read_csv(csv_path)
    required_cols = {"color_name", "hex", "R", "G", "B"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"colors.csv must contain columns: {required_cols}")
    return df
