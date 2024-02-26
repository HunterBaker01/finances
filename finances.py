import pandas as pd
import numpy as np
from datetime import date

# Data Frame that will hold the information
records = pd.read_csv('finances.csv')

# Create the function that will track daily finances
def daily(date: str = date.today(), earned: float = 0, time: int = 0, fun_exp: float = 0, fun_category: str = np.nan, bills_exp: float = 0, bills_category: str = np.nan):
    # Call in the global dataframe
    global records

    # Define variables based on the amounts given
    tax = earned * .35
    total_after_tax = earned - tax
    save = (earned - tax) * .60
    fun = (earned - tax) * .40
    total_expense = bills_exp + fun_exp

    # Define variables based on the previous row
    prev_total = records.iloc[-1, 3]
    prev_tax = records.iloc[-1, 4]
    prev_save = records.iloc[-1, 6]
    prev_fun = records.iloc[-1, 7]
    prev_exp = records.iloc[-1, 11]
    prev_total_after_tax = records.iloc[-1, 5]

    # Update the dataframe
    new_data = pd.DataFrame({'Date': [date], 'Amount': [earned], 'Time (min)': time,
                            'Total': [prev_total + earned], 'Total Tax': [prev_tax + tax],
                            'Total After Tax': [prev_total_after_tax + total_after_tax],
                            'Save/Bills': [prev_save + save - bills_exp], 'Fun Money': [prev_fun + fun - fun_exp],
                            'Expenses': [total_expense], 'Bills Category': [bills_category],
                            'Fun Category': [fun_category], 'Total Expenses': [prev_exp + total_expense]})
    
    records = pd.concat([records, new_data])
    return records


records.to_csv('finances.csv', sep=',', index=False, encoding='utf-8')