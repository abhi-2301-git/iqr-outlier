import pandas as pd
import numpy as np

def detect_outliers(data):
    """
    Detect outliers using IQR method.
    Returns a list of outliers.
    """
    if isinstance(data,list):
        data = pd.Series(data)

    Q1 = np.percentile(data,25)
    Q3 = np.percentile(data,75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = data[(data < lower_bound) | (data > upper_bound)]


    return outliers.tolist()