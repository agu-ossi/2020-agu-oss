"""A second sample module to clean data."""

import pandas as pd

def open_and_clean(url):
    """
    A function that is designed to clean up  data downloaded  from
    the Berkely earth website. This function assumes that your data
    are always in the same format.

    Parameters
    ----------
    url : string
        Path to the data  from the Berkeley earth  website

    Returns
    -------
    Pandas.DataFrame

    """

    temp_df = pd.read_csv(url,
                          skiprows=69,
                          delim_whitespace=True)

    all_cols = temp_df.columns[2:]

    # Remove the last row
    temp_df = temp_df.iloc[:, :-1]

    # CLEANUP: Drop the commas from the column names & Add a day column
    temp_df.columns = [acol.replace(',', '') for acol in all_cols]
    temp_df = temp_df.assign(Day=1)

    # Finally create a date time column
    temp_df["date"] = pd.to_datetime(temp_df[['Year', 'Month', 'Day']])

    return temp_df.set_index("date")
