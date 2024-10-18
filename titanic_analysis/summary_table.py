import pandas as pd
def create_summary_table(data):
    summary = {
        'Feature Name': data.columns,
        'Data Type': data.dtypes.values,
        'Number of Unique Values': data.nunique().values,
        'Has Missing Values?': data.isnull().any().values
    } 
    summary_data = pd.DataFrame(summary)
    return summary_data