"""
detect_color.py
Nearest-neighbor color name matching given an (R, G, B) pixel value.
"""

import pandas as pd


def get_color_name(R: int, G: int, B: int, color_df: pd.DataFrame) -> str:
    """
    Return the name of the closest matching color in color_df to the
    given R, G, B values, using minimum absolute-distance sum.
    """
    min_distance = float("inf")
    closest_name = "Unknown"

    for _, row in color_df.iterrows():
        distance = (
            abs(R - int(row["R"]))
            + abs(G - int(row["G"]))
            + abs(B - int(row["B"]))
        )
        if distance < min_distance:
            min_distance = distance
            closest_name = row["color_name"]

    return closest_name


if __name__ == "__main__":
    # quick manual test
    from utils import load_colors

    df = load_colors("data/colors.csv")
    print(get_color_name(200, 10, 55, df))   # should be close to Crimson
    print(get_color_name(30, 140, 30, df))   # should be close to ForestGreen/Green
