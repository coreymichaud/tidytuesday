import os
import contextlib
import pydytuesday

def download_week(year: int, week_num: int, output_dir: str = "data") -> None:
    """
    Downloads the specified week of data from the PydyTuesday library.

    Args:
        year (int): The year of the week to download.
        week_num (int): The week number to download.
        output_dir (str): The directory to save the downloaded data. Defaults to "data".
    """

    # Creates data directory within the week folder this is called from
    os.makedirs(output_dir, exist_ok=True)

    # Downloads data into data/ folder
    with contextlib.chdir(output_dir):
        pydytuesday.get_week(year, week_num)