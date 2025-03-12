import pandas as pd

from iqr_outlier.detection import detect_outliers
from iqr_outlier.removal import remove_outliers


df= pd.read_csv(r'E:\CODE\Python\Projects\iqr_outliers\sample.csv')
print("defore removal:", df['marks'].value_counts().sum())
print("Outliers detected:", detect_outliers(df['marks']))
df['marks'] = remove_outliers(df['marks'])
print("After removal:", df['marks'].value_counts().sum())
